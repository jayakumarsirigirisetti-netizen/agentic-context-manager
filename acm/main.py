from fastapi import FastAPI
from acm.memory.store import MemoryStore
from acm.core.memory_object import MemoryObject
from acm.core.importance import compute_importance
from acm.core.embeddings import EmbeddingEngine

app = FastAPI(title="Agentic Context Manager")

embedder = EmbeddingEngine()
store = MemoryStore(embedding_dim=384)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/memory/write")
def write_memory(content: str):
    embedding = embedder.embed(content)
    importance = compute_importance(
        intent_match=0.8,
        novelty=0.7,
        recency=1.0
    )
    memory = MemoryObject.create(
        content=content,
        importance=importance,
        embedding=embedding
    )
    store.write(memory)
    return {"stored": memory}

@app.post("/memory/search")
def search_memory(query: str):
    query_embedding = embedder.embed(query)
    return store.search(query_embedding)
