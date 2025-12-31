from datetime import datetime, timedelta

from acm.core.memory_object import MemoryObject
from acm.core.summarizer import summarize_memories
from acm.core.embeddings import EmbeddingEngine
from acm.core.importance import compute_importance

embedder = EmbeddingEngine()

# Create several low-importance memories
raw_memories = []

contents = [
    "Minor UI alignment issue",
    "Button color slightly off",
    "Tooltip text typo",
    "Spacing issue on settings page",
]

for i, text in enumerate(contents):
    importance = compute_importance(
        content=text,
        intent_match=0.2,
        novelty=0.1,
        recency=0.2,
    )

    mem = MemoryObject(
        id=f"m{i}",
        content=text,
        importance=importance,
        embedding=embedder.embed(text),
        created_at=datetime.utcnow() - timedelta(days=20),
    )

    raw_memories.append(mem)

# ---- Summarize ----
summary_text = summarize_memories(raw_memories)

summary_importance = compute_importance(
    content=summary_text,
    intent_match=0.4,
    novelty=0.6,
    recency=0.9,
)

summary_memory = MemoryObject.create(
    content=summary_text,
    importance=summary_importance,
    embedding=embedder.embed(summary_text),
)

print("SUMMARY TEXT:")
print(summary_text)

print("\nSUMMARY IMPORTANCE:", summary_memory.importance)
print("SUMMARY EMBEDDING DIM:", len(summary_memory.embedding))
print("SUMMARY CREATED AT:", summary_memory.created_at)

print("\nORIGINAL MEMORY COUNT:", len(raw_memories))
print("COMPRESSED MEMORY COUNT: 1")

