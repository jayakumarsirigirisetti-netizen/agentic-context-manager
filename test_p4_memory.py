from acm.core.memory_object import MemoryObject
from acm.core.embeddings import EmbeddingEngine
from acm.core.importance import compute_importance

# Initialize embedding engine
embedder = EmbeddingEngine()

content = "User reports login timeout error"

# Simulated importance signals (valid values: 0.0–1.0)
intent_match = 0.9   # highly relevant to current task
novelty = 0.7        # somewhat new information
recency = 1.0        # just happened

importance = compute_importance(
    content=content,
    intent_match=intent_match,
    novelty=novelty,
    recency=recency,
)

memory = MemoryObject.create(
    content=content,
    importance=importance,
    embedding=embedder.embed(content),
)

print("ID:", memory.id)
print("CONTENT:", memory.content)
print("IMPORTANCE:", memory.importance)
print("EMBEDDING DIM:", len(memory.embedding))
print("CREATED_AT:", memory.created_at)

