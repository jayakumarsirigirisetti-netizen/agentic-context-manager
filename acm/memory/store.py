from typing import List
from acm.core.memory_object import MemoryObject
from acm.memory.vector_store import VectorStore
from acm.core.decay import apply_decay

class MemoryStore:
    def __init__(self, embedding_dim: int, forget_threshold: float = 0.25):
        self.memories: List[MemoryObject] = []
        self.vector_store = VectorStore(embedding_dim)
        self.forget_threshold = forget_threshold

    def write(self, memory: MemoryObject):
        self.memories.append(memory)
        self.vector_store.add(memory.embedding, memory.id)

    def list(self) -> List[MemoryObject]:
        return self.memories

    def prune(self):
        kept = []
        for m in self.memories:
            m.importance = apply_decay(m.importance, m.created_at)
            if m.importance >= self.forget_threshold:
                kept.append(m)
        self.memories = kept

    def search(self, query_embedding: list, top_k: int = 5):
        self.prune()
        ids = self.vector_store.search(query_embedding, top_k)
        return [m for m in self.memories if m.id in ids]
