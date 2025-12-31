from acm.core.decay import apply_decay
from acm.core.summarizer import summarize_memories
from acm.core.memory_object import MemoryObject
from acm.core.embeddings import EmbeddingEngine
from acm.core.importance import compute_importance
from acm.core.config import ContextConfig
from datetime import datetime


class AgentLoop:
    def __init__(self, llm_provider):
        self.llm = llm_provider
        self.config = ContextConfig()
        self.embedder = EmbeddingEngine()
        self.memories = []

    # -------------------------
    # MEMORY SELECTION
    # -------------------------
    def select_memories(self):
        selected = []
        for m in self.memories:
            effective = apply_decay(m.importance, m.created_at)
            if effective >= self.config.importance_threshold:
                selected.append(m)
        return selected

    # -------------------------
    # CONTEXT BUILDING
    # -------------------------
    def build_context(self, task, memories):
        memory_text = "\n".join([f"- {m.content}" for m in memories])
        return f"""
TASK:
{task}

RELEVANT MEMORY:
{memory_text}

Respond clearly and concisely.
"""

    # -------------------------
    # MEMORY WRITE-BACK
    # -------------------------
    def store_response(self, task, response):
        importance = compute_importance(
            content=response,
            intent_match=0.8,
            novelty=0.6,
            recency=1.0,
        )

        memory = MemoryObject.create(
            content=response,
            importance=importance,
            embedding=self.embedder.embed(response),
        )

        self.memories.append(memory)

    # -------------------------
    # SUMMARIZATION STEP
    # -------------------------
    def summarize_if_needed(self):
        if len(self.memories) > 5:
            summary_text = summarize_memories(self.memories)
            summary_importance = compute_importance(
                content=summary_text,
                intent_match=0.7,
                novelty=0.6,
                recency=1.0,
            )

            summary_memory = MemoryObject.create(
                content=summary_text,
                importance=summary_importance,
                embedding=self.embedder.embed(summary_text),
            )

            self.memories = [summary_memory]

    # -------------------------
    # MAIN LOOP
    # -------------------------
    def run(self, task):
        relevant = self.select_memories()
        context = self.build_context(task, relevant)
        response = self.llm.complete(context)

        self.store_response(task, response)
        self.summarize_if_needed()

        return response

