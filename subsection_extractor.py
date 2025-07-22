# subsection_extractor.py — Paragraph-level refinement within top sections

import pymupdf  # PyMuPDF
import re
from typing import Dict, Any, List
from sentence_transformers import SentenceTransformer
import numpy as np

class SubsectionExtractor:
    """
    Extracts and refines the most relevant sub-sections (3-sentence windows)
    from a given section's page range.
    """

    def __init__(self):
        # Reuse the same embedding model for consistency if needed
        # (or accept a SemanticAnalyzer instance to share)
        pass

    def _get_page_text(self, pdf_path: str, page_no: int) -> str:
        """
        Load a single page's full text from PDF.
        """
        doc = pymupdf.open(pdf_path)
        page = doc.load_page(page_no - 1)
        text = page.get_text("text")
        doc.close()
        return text

    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Naïve sentence splitting based on punctuation.
        """
        sentences = re.split(r'(?<=[\.\?\!])\s+', text.strip())
        return [s for s in sentences if len(s) > 0]

    def _window_scores(
        self,
        sentences: List[str],
        analyzer,            # SemanticAnalyzer instance
        scorer,              # RelevanceScorer instance
        persona_vector: np.ndarray
    ) -> List[Dict[str, Any]]:
        """
        Slide a 3-sentence window, score each window semantically.
        """
        windows = []
        for i in range(len(sentences) - 2):
            window_text = " ".join(sentences[i : i + 3])
            vec = analyzer.model.encode(window_text, convert_to_numpy=True)
            # pure semantic for subsection
            sim = float(np.dot(persona_vector, vec) / (
                np.linalg.norm(persona_vector) * np.linalg.norm(vec) + 1e-6
            ))
            windows.append({
                "start_idx": i,
                "text": window_text,
                "score": sim
            })
        return windows

    def refine_section(
        self,
        pdf_path: str,
        start_page: int,
        end_page: int,
        section_title: str,
        semantic_analyzer,
        relevance_scorer
    ) -> Dict[str, Any]:
        """
        For a given section, extract the top 1-2 most relevant
        3-sentence windows across its pages.
        Returns the best window text and its page.
        """
        best_windows = []
        persona_vec = semantic_analyzer.persona_task_vector

        # Iterate pages in section
        for pg in range(start_page, end_page + 1):
            full_text = self._get_page_text(pdf_path, pg)
            sentences = self._split_into_sentences(full_text)
            if len(sentences) < 3:
                continue

            windows = self._window_scores(sentences, semantic_analyzer, relevance_scorer, persona_vec)
            # pick top window from this page
            if windows:
                top = max(windows, key=lambda w: w["score"])
                best_windows.append({**top, "page": pg})

        # select overall top 1-2 windows
        best_windows.sort(key=lambda w: w["score"], reverse=True)
        selected = best_windows[:2]

        # Concatenate texts if two windows
        refined_text = " ".join([w["text"] for w in selected])
        page = selected[0]["page"] if selected else start_page

        return {
            "text": refined_text,
            "page": page
        }
