#!/usr/bin/env python3
"""
Round-1B | Persona-Aware PDF Pipeline
------------------------------------
CLI
    python main.py <input_dir> <output_dir>

• Reads  challenge1b_input.json  from <input_dir>.
• Runs the original Round-1A extractor *in parallel* on every PDF
  (each worker opens the file from bytes once).
• Embeds + ranks sections with Granite-107 M embeddings and BM25.
• Refines best sections (thread-pool) and writes  challenge1b_output.json
  to <output_dir>.
"""

import json
import os
import sys
from datetime import datetime, timezone
from typing import Dict, List

import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed


# Round-1B modules
from semantic_analyzer    import SemanticAnalyzer
from relevance_scorer     import RelevanceScorer
from subsection_extractor import SubsectionExtractor

# Disable oneDNN heuristics for small-CPU images (optional but safe)
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


# ─────────────────────────  Helpers  ──────────────────────────
def _extract_outline_blob(pdf_path: str) -> Dict:
    """Worker: run Round-1A on a PDF file path."""
    from r1a.enhanced_pdf_extractor import process_pdf_enhanced
    return process_pdf_enhanced(pdf_path)


def _load_input(inp_dir: str) -> Dict:
    with open(os.path.join(inp_dir, "challenge1b_input.json"), encoding="utf-8") as fh:
        return json.load(fh)


def _write_output(out_dir: str, data: Dict) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "challenge1b_output.json"), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


# ─────────────────────────  Main  ──────────────────────────
def run_pipeline(input_dir: str, output_dir: str) -> None:

    req = _load_input(input_dir)

    metadata = {
        "input_documents": [d["filename"] for d in req["documents"]],
        "persona":         req["persona"]["role"],
        "job_to_be_done":  req["job_to_be_done"]["task"],
        "processing_timestamp": datetime.now(timezone.utc).isoformat()
    }

    # 1.  Parallel outline extraction (Round-1A)
    pdf_dir  = os.path.join(input_dir, "PDFs")
    outlines: Dict[str, Dict] = {}
    pdf_paths = [os.path.join(pdf_dir, d["filename"]) for d in req["documents"]]
    max_w = min(len(req["documents"]), multiprocessing.cpu_count())
    with ProcessPoolExecutor(max_workers=max_w) as pool:
        fut2doc = {}
        for pdf_path, d in zip(pdf_paths, req["documents"]):
            fut2doc[pool.submit(_extract_outline_blob, pdf_path)] = d
        for fut in as_completed(fut2doc):
            doc = fut2doc[fut]
            outlines[doc["filename"]] = fut.result()

    # 2.  Initialise semantic engine + ranker + subsection extractor
    model_dir = os.path.abspath("models")          # Models are here
    sem   = SemanticAnalyzer(model_dir=model_dir, model = "granite-embedding-107m-multilingual")
    rank  = RelevanceScorer()
    subex = SubsectionExtractor()

    sem.embed_persona_and_task(metadata["persona"], metadata["job_to_be_done"])
    rank.extract_task_keywords(metadata["job_to_be_done"])

    extracted_sections:  List[Dict] = []
    subsection_analysis: List[Dict] = []

    # 3.  Process each PDF
    for d in req["documents"]:
        fname   = d["filename"]
        outline = outlines.get(fname, {}).get("outline", [])

        # inject cover-page title
        title_txt = outlines[fname].get("title", "").strip() if fname in outlines else ""
        if title_txt:
            outline.insert(0, {"level": "H1", "text": title_txt, "page": 1})

        if not outline:
            continue

        sections = sem.embed_sections(outline, fname)
        for s in sections:
            s["semantic_analyzer"] = sem

        top5 = rank.rank_sections(sections)

        pdf_path = os.path.join(pdf_dir, fname)

        # Thread-pool: refine five sections in parallel
        def _ref(sec):
            return subex.refine_section(
                pdf_path, sec.get("start_page", sec["page"]), sec.get("end_page", sec["page"]),
                sec["title"], sem, rank
            )

        with ThreadPoolExecutor(max_workers=4) as tpool:
            refined_list = list(tpool.map(_ref, top5))

        for sec, refined in zip(top5, refined_list):
            extracted_sections.append({
                "document": fname,
                "section_title": sec["title"],
                "importance_rank": sec["rank"],
                "page_number": sec["page"]
            })
            subsection_analysis.append({
                "document": fname,
                "refined_text": refined["text"],
                "page_number": refined["page"]
            })

    # 4.  Write output
    extracted_sections.sort(key=lambda x: x["importance_rank"])
    _write_output(output_dir, {
        "metadata":            metadata,
        "extracted_sections":  extracted_sections,
        "subsection_analysis": subsection_analysis
    })


# ─────────────────────────  Entrypoint  ──────────────────────────
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_dir> <output_dir>")
        sys.exit(1)

    run_pipeline(sys.argv[1], sys.argv[2])
