# semantic_analyzer.py  —  Offline embedding loader (Granite-107 M multilingual)
# ---------------------------------------------------------------
# • Batched encodes for headings
# • Per-page sentence-vector cache (shared by SubsectionExtractor)
# • Fully offline via HF_HUB_OFFLINE / TRANSFORMERS_OFFLINE
# ---------------------------------------------------------------

import os
from pathlib import Path
from typing import List, Dict, Tuple

import numpy as np
from sentence_transformers import SentenceTransformer #type: ignore


class SemanticAnalyzer:
    """
    Lightweight wrapper around the IBM Granite-107 M multilingual
    embedding model, with conveniences for:
        • persona+task vector
        • batched section embeddings
        • shared sentence-level cache for subsections
    """

    # -------- initialisation -------------------------------------------------
    def __init__(self, model_dir: str = "./models", model = "all-MiniLM-L6-v2") -> None:
        """
        `model_dir` must contain the model specified below
        """
        model = model
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"

        model_path = Path(model_dir) / model
        if not model_path.exists():
            raise FileNotFoundError(
                f"Granite model not found at {model_path}.\n"
                "Make sure you copied it into the image before running."
            )

        # Load once; remains resident for all embeddings
        self.model = SentenceTransformer(str(model_path), local_files_only=True)

        # persona vector & per-page cache
        self.persona_task_vector: np.ndarray | None = None
        self._sentence_cache: Dict[str, Tuple[List[str], np.ndarray]] = {}

    # -------- high-level helpers --------------------------------------------
    def embed_persona_and_task(self, persona: str, task: str) -> None:
        """Create & store a 768-d vector for the user intent."""
        prompt = f"{persona}. {task}"
        self.persona_task_vector = self.model.encode(
            prompt, convert_to_numpy=True
        )

    def embed_sections(self, outline: list, doc_id: str) -> list:
        """
        Batch-encode every heading in `outline`.
        Returns a list of section dicts ready for the ranker.
        """
        if not outline:
            return []

        texts = [sec["text"] for sec in outline]
        vectors = self.model.encode(
            texts,
            batch_size=64,           # adjust if you want smaller RAM spikes
            convert_to_numpy=True,
            show_progress_bar=False
        )

        sections = []
        for sec, vec in zip(outline, vectors):
            page = sec.get("page", 1)
            sections.append(
                {
                    "doc_id": doc_id,
                    "title": sec["text"],
                    "vector": vec,
                    "page": page,
                    "start_page": page,
                    "end_page": page,
                }
            )
        return sections

    # -------- cosine helper --------------------------------------------------
    def similarity(self, section_vector: np.ndarray) -> float:
        """
        Cosine similarity between persona/task vector and an arbitrary vector.
        """
        if self.persona_task_vector is None:
            raise RuntimeError("Call embed_persona_and_task() first.")

        dot = float(np.dot(self.persona_task_vector, section_vector))
        norm = (
            np.linalg.norm(self.persona_task_vector)
            * np.linalg.norm(section_vector)
            + 1e-9
        )
        return dot / norm

    # -------- cache interface for SubsectionExtractor -----------------------
    def get_sentence_vectors(
        self, page_text: str, batch_size: int = 64
    ) -> Tuple[List[str], np.ndarray]:
        """
        Return (sentence_list, 2-d array[ n × 768 ]).
        Results are memoised so the same page is encoded only once.
        """
        cached = self._sentence_cache.get(page_text)
        if cached is not None:
            return cached

        sentences = _simple_sentence_split(page_text)
        if not sentences:
            self._sentence_cache[page_text] = ([], np.empty((0, 768)))
            return self._sentence_cache[page_text]

        vecs = self.model.encode(
            sentences,
            batch_size=batch_size,
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        self._sentence_cache[page_text] = (sentences, vecs)
        return self._sentence_cache[page_text]


# ---------------------------------------------------------------------------
# tiny fallback sentence splitter (kept here to avoid extra imports)
# ---------------------------------------------------------------------------
import re

_SENT_SPLIT_RE = re.compile(r"(?<=[\.\?!])\s+")


def _simple_sentence_split(text: str) -> List[str]:
    return [s for s in _SENT_SPLIT_RE.split(text.strip()) if s]
