#!/usr/bin/env python3
"""
Round 1B – Pipeline Orchestrator

CLI
----
python main.py <input_dir> <output_dir>

• Reads  challenge1b_input.json  from <input_dir>.
• Extracts outlines from every PDF (parallel, using the Round 1A extractor).
• Embeds, ranks and refines sections with the Round 1B modules.
• Writes challenge1b_output.json to <output_dir>.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List

import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

# ────────────────────────────────────────────────────────────
#  Local Round 1B modules
# ────────────────────────────────────────────────────────────
from semantic_analyzer import SemanticAnalyzer
from relevance_scorer import RelevanceScorer
from subsection_extractor import SubsectionExtractor


# ────────────────────────────────────────────────────────────
#  Helper for process-safe PDF extraction (runs in worker)
# ────────────────────────────────────────────────────────────
def _extract_outline(pdf_path: str) -> Dict:
    """Return the outline dict produced by the Round 1A extractor."""
    # Import inside the worker to avoid PyMuPDF state sharing
    from r1a.enhanced_pdf_extractor import process_pdf_enhanced

    return process_pdf_enhanced(pdf_path)


# ────────────────────────────────────────────────────────────
#  I/O helpers
# ────────────────────────────────────────────────────────────
def _load_input(input_dir: str) -> Dict:
    path = os.path.join(input_dir, "challenge1b_input.json")
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _write_output(output_dir: str, data: Dict) -> None:
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "challenge1b_output.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


# ────────────────────────────────────────────────────────────
#  Main pipeline
# ────────────────────────────────────────────────────────────
def run_pipeline(input_dir: str, output_dir: str) -> None:
    raw = _load_input(input_dir)

    # 1. Metadata ----------------------------------------------------------------
    metadata = {
        "input_documents": [d["filename"] for d in raw["documents"]],
        "persona": raw["persona"]["role"],
        "job_to_be_done": raw["job_to_be_done"]["task"],
        "processing_timestamp": datetime.utcnow().isoformat()
    }

    # 2. Parallel outline extraction (Round 1A) ----------------------------------
    pdf_paths = [os.path.join(input_dir, d["filename"]) for d in raw["documents"]]
    outlines: Dict[str, Dict] = {}

    max_workers = min(len(pdf_paths), multiprocessing.cpu_count())
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        future_to_doc = {
            pool.submit(_extract_outline, p): d for p, d in zip(pdf_paths, raw["documents"])
        }
        for fut in as_completed(future_to_doc):
            doc = future_to_doc[fut]
            outlines[doc["filename"]] = fut.result()

    # 3. Initialise semantic & relevance modules ---------------------------------
    model_dir = os.path.join(input_dir, "models")
    sem = SemanticAnalyzer(model_dir=model_dir)
    scorer = RelevanceScorer()
    sub_ext = SubsectionExtractor()

    # Persona / task embedding once
    sem.embed_persona_and_task(metadata["persona"], metadata["job_to_be_done"])
    scorer.extract_task_keywords(metadata["job_to_be_done"])

    # 4. Loop over documents – embedding, ranking, refinement --------------------
    extracted_sections: List[Dict] = []
    subsection_analysis: List[Dict] = []

    for doc in raw["documents"]:
        doc_id = doc["filename"]
        outline = outlines.get(doc_id, {}).get("outline", [])

        # 4-a  Embed each section heading
        sections = sem.embed_sections(outline, doc_id)

        # Attach analyzer reference required by scorer
        for s in sections:
            s["semantic_analyzer"] = sem

        # 4-b  Rank and keep top-5
        top5 = scorer.rank_sections(sections)

        for sec in top5:
            extracted_sections.append({
                "document": doc_id,
                "section_title": sec["title"],
                "importance_rank": sec["rank"],
                "page_number": sec["page"]
            })

            # 4-c  Refine subsection text
            refined = sub_ext.refine_section(
                pdf_path=os.path.join(input_dir, doc_id),
                start_page=sec.get("start_page", sec["page"]),
                end_page=sec.get("end_page", sec["page"]),
                section_title=sec["title"],
                semantic_analyzer=sem,
                relevance_scorer=scorer
            )
            subsection_analysis.append({
                "document": doc_id,
                "refined_text": refined["text"],
                "page_number": refined["page"]
            })

    # 5. Output ------------------------------------------------------------------
    _write_output(
        output_dir,
        {
            "metadata": metadata,
            "extracted_sections": extracted_sections,
            "subsection_analysis": subsection_analysis
        }
    )


# ────────────────────────────────────────────────────────────
#  Entry-point guard
# ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_dir> <output_dir>")
        sys.exit(1)

    run_pipeline(sys.argv[1], sys.argv[2])
