# relevance_scorer.py – Granite-278 M edition
# Hybrid ranking: 80 % semantic cosine, 20 % BM25 keyword match
# --------------------------------------------------------------

from rank_bm25 import BM25Okapi
import numpy as np
import re
from typing import List, Dict, Sequence, Set

# optional, tiny English stop-list
_STOP = {
    "the", "a", "an", "of", "to", "for", "and", "in", "on",
    "with", "at", "by", "from", "is", "are", "be", "this",
    "that", "it", "its", "as", "your", "you"
}


class RelevanceScorer:
    """
    Ranks document sections by combining
      • cosine similarity from IBM Granite embeddings
      • BM25 keyword relevance for explicit task terms
    """

    def __init__(
        self,
        bm25_k: float = 1.5,
        bm25_b: float = 0.75,
        semantic_weight: float = 0.80,   # ↑ give Granite more influence
        max_return: int = 5
    ):
        self.bm25_k = bm25_k
        self.bm25_b = bm25_b
        self.semantic_weight = semantic_weight
        self.max_return = max_return

        self.task_keywords: List[str] = []
        self.bm25: BM25Okapi | None = None

    # ──────────────────────────────────────────────────────────
    # 1  Keyword preparation
    # ──────────────────────────────────────────────────────────
    def extract_task_keywords(self, task: str) -> List[str]:
        tokens = [t for t in re.findall(r"\w+", task.lower())
                  if t not in _STOP and len(t) > 1]
        self.task_keywords = tokens or [task.lower()]
        return self.task_keywords

    # ──────────────────────────────────────────────────────────
    # 2  BM25 index
    # ──────────────────────────────────────────────────────────
    def _fit_bm25(self, sections: Sequence[Dict]) -> None:
        corpus = [re.findall(r"\w+", s["title"].lower()) for s in sections]
        self.bm25 = BM25Okapi(corpus, k1=self.bm25_k, b=self.bm25_b)

    # ──────────────────────────────────────────────────────────
    # 3  Section scoring
    # ──────────────────────────────────────────────────────────
    def _score_sections(
        self,
        sections: Sequence[Dict],
        analyzer          # SemanticAnalyzer instance
    ) -> List[Dict]:
        self._fit_bm25(sections)

        # pre-compute BM25 scores (vector of floats)
        bm25_all = self.bm25.get_scores(self.task_keywords)

        scored: List[Dict] = []
        vec_task = analyzer.persona_task_vector

        for idx, sec in enumerate(sections):
            bm25_score = float(bm25_all[idx])

            # cosine similarity
            vec_sec = sec["vector"]
            sim = np.dot(vec_task, vec_sec) / (
                np.linalg.norm(vec_task) * np.linalg.norm(vec_sec) + 1e-9
            )

            combo = (
                self.semantic_weight * sim +
                (1.0 - self.semantic_weight) * (bm25_score / (bm25_score + 3.0))
            )

            scored.append({
                **sec,
                "bm25_score": bm25_score,
                "semantic_score": sim,
                "combined_score": combo
            })
        return scored

    # ──────────────────────────────────────────────────────────
    # 4  Public API
    # ──────────────────────────────────────────────────────────
    def rank_sections(self, sections: List[Dict]) -> List[Dict]:
        if not sections:
            return []

        analyzer = sections[0]["semantic_analyzer"]

        # ensure keywords present (for unit tests)
        if not self.task_keywords:
            self.extract_task_keywords("")

        if len(sections) < 80:
            tmp_sem_weight = 1.0          # go full-semantic for tiny corpora
            prev = self.semantic_weight
            self.semantic_weight = tmp_sem_weight
            scored = self._score_sections(sections, analyzer)
            self.semantic_weight = prev
        else:
            scored = self._score_sections(sections, analyzer)

        scored = self._score_sections(sections, analyzer)

        # sort & deduplicate by title (case-insensitive)
        sorted_scored = sorted(
            scored, key=lambda s: s["combined_score"], reverse=True
        )

        unique_titles: Set[str] = set()
        top: List[Dict] = []
        for s in sorted_scored:
            norm_title = s["title"].strip().lower()
            if norm_title not in unique_titles:
                unique_titles.add(norm_title)
                top.append(s)
            if len(top) == self.max_return:
                break

        for rank, sec in enumerate(top, start=1):
            sec["rank"] = rank

        return top
