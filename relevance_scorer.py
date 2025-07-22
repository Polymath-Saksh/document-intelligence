# relevance_scorer.py — Hybrid BM25 + semantic similarity ranking

from rank_bm25 import BM25Okapi
import numpy as np
import re
from typing import List, Dict

class RelevanceScorer:
    """
    Combines semantic similarity (from SemanticAnalyzer) with BM25
    lexical relevance to rank document sections.
    """

    def __init__(self, bm25_k: float = 1.5, bm25_b: float = 0.75, semantic_weight: float = 0.7):
        self.bm25_k = bm25_k
        self.bm25_b = bm25_b
        self.semantic_weight = semantic_weight
        self.task_keywords = []
        self.bm25 = None

    def extract_task_keywords(self, task: str) -> List[str]:
        """
        Tokenize and normalize job-to-be-done text into key terms.
        """
        tokens = re.findall(r'\w+', task.lower())
        # Optionally filter stopwords here if needed
        self.task_keywords = tokens
        return tokens

    def fit_bm25(self, sections: List[Dict]):
        """
        Build BM25 index over section titles (and optional snippet) token lists.
        """
        corpus = [re.findall(r'\w+', sec["title"].lower()) for sec in sections]
        self.bm25 = BM25Okapi(corpus, k1=self.bm25_k, b=self.bm25_b)

    def score_sections(self, sections: List[Dict], semantic_analyzer):
        """
        Compute BM25 + semantic scores for each section and return the
        list enriched with 'bm25_score', 'semantic_score', 'combined_score'.
        """
        # Build / rebuild the BM25 index once
        self.fit_bm25(sections)

        # Pre-compute scores for the query (= task keywords)
        bm25_all = self.bm25.get_scores(self.task_keywords)  # ← API is get_scores

        scored = []
        for idx, sec in enumerate(sections):
            bm25_score      = float(bm25_all[idx])
            semantic_score  = semantic_analyzer.similarity(sec["vector"])

            combined = (self.semantic_weight * semantic_score +
                        (1 - self.semantic_weight) * (bm25_score /
                        (bm25_score + 1e-6)))          # normalise

            scored.append({
                **sec,
                "bm25_score":      bm25_score,
                "semantic_score":  semantic_score,
                "combined_score":  combined
            })
        return scored

    def rank_sections(self, sections: List[Dict]) -> List[Dict]:
        """
        Rank the sections and return the best five.

        Expects that self.task_keywords has already been
        filled by extract_task_keywords(). If not, it
        will fall back to an empty keyword list.
        """

        # ---- 1.  ensure task keywords ---------------------------------
        task = sections[0].get("persona_task_text", "")
        if task:                       # only when the key is present
            self.extract_task_keywords(task)
        # (else: leave whatever is already in self.task_keywords)

        # ---- 2.  score and sort ---------------------------------------
        scored = self.score_sections(sections,
                                    semantic_analyzer=sections[0]["semantic_analyzer"])

        ranked = sorted(scored,
                        key=lambda x: x["combined_score"],
                        reverse=True)[:5]

        for i, sec in enumerate(ranked, start=1):
            sec["rank"] = i
        return ranked
