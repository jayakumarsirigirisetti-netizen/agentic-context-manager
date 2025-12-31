from datetime import datetime, timedelta

from acm.core.memory_object import MemoryObject
from acm.core.decay import apply_decay
from acm.core.embeddings import EmbeddingEngine
from acm.core.importance import compute_importance
from acm.core.config import ContextConfig

embedder = EmbeddingEngine()
config = ContextConfig()

# ---- Memory 1: recent & important ----
recent_content = "Critical production outage in auth service"

recent_importance = compute_importance(
    content=recent_content,
    intent_match=0.95,
    novelty=0.9,
    recency=1.0,
)

recent_memory = MemoryObject(
    id="recent",
    content=recent_content,
    importance=recent_importance,
    embedding=embedder.embed(recent_content),
    created_at=datetime.utcnow() - timedelta(days=1),
)

recent_effective = apply_decay(
    recent_memory.importance,
    recent_memory.created_at
)

# ---- Memory 2: old & weak ----
old_content = "Minor UI typo in settings page"

old_importance = compute_importance(
    content=old_content,
    intent_match=0.2,
    novelty=0.1,
    recency=0.1,
)

old_memory = MemoryObject(
    id="old",
    content=old_content,
    importance=old_importance,
    embedding=embedder.embed(old_content),
    created_at=datetime.utcnow() - timedelta(days=30),
)

old_effective = apply_decay(
    old_memory.importance,
    old_memory.created_at
)

print("Recent effective importance:", recent_effective)
print("Old effective importance:", old_effective)
print("Threshold:", config.importance_threshold)

print("\nShould keep recent?",
      recent_effective >= config.importance_threshold)

print("Should keep old?",
      old_effective >= config.importance_threshold)

