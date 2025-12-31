import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.ids = []

    def add(self, embedding: list, memory_id: str):
        vec = np.array([embedding]).astype("float32")
        self.index.add(vec)
        self.ids.append(memory_id)

    def search(self, embedding: list, top_k: int = 5):
        vec = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(vec, top_k)
        results = []
        for idx in indices[0]:
            if idx < len(self.ids):
                results.append(self.ids[idx])
        return results
