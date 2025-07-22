# semantic_analyzer.py — Offline embedding loader

import os
from sentence_transformers import SentenceTransformer
import numpy as np

class SemanticAnalyzer:
    """
    Loads embedding model from bundled local directory.
    """

    def __init__(self, model_dir: str = "./models"):
        """
        model_dir: path containing 'all-MiniLM-L6-v2' folder
        """
        model_path = os.path.join(model_dir, "all-MiniLM-L6-v2")
        
        # Force offline mode to prevent any network calls
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        
        try:
            self.model = SentenceTransformer(model_path, local_files_only=True)
        except Exception as e:
            print(f"Failed to load model from {model_path}: {e}")
            raise
            
        self.persona_task_vector = None

    def embed_persona_and_task(self, persona: str, task: str):
        """
        Creates a single vector representing the persona + job-to-be-done.
        """
        combined = f"{persona}. {task}"
        self.persona_task_vector = self.model.encode(combined, convert_to_numpy=True)

    def embed_sections(self, outline: list, doc_id: str) -> list:
        """
        Embeds each section title and returns list with vectors.
        """
        embeddings = []
        for sec in outline:
            text = sec["text"]
            vec = self.model.encode(text, convert_to_numpy=True)
            
            # Extract page info (assuming sec has 'page' field from Round 1A)
            page_num = sec.get("page", 1)
            
            embeddings.append({
                "doc_id": doc_id,
                "title": text,
                "vector": vec,
                "page": page_num,
                "start_page": page_num,  # For compatibility with subsection extractor
                "end_page": page_num
            })
        return embeddings

    def similarity(self, section_vector: np.ndarray) -> float:
        """
        Cosine similarity between persona/task vector and section vector.
        """
        if self.persona_task_vector is None:
            raise ValueError("Persona/task vector not initialized.")
        
        dot = np.dot(self.persona_task_vector, section_vector)
        norm = np.linalg.norm(self.persona_task_vector) * np.linalg.norm(section_vector)
        return float(dot / norm) if norm > 0 else 0.0
