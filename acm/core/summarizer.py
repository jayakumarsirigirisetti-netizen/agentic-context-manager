def summarize_memories(memories: list) -> str:
    """
    Simple extractive summary (LLM-ready later)
    """
    contents = [m.content for m in memories]
    return " | ".join(contents[:3])
