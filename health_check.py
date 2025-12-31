from acm.memory import MemoryStore

EMBEDDING_DIM = 1536

m = MemoryStore(embedding_dim=EMBEDDING_DIM)

count = m.vector_store.index.ntotal

print("✅ ACM healthy | Vector memory size:", count)

