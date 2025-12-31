def compute_importance(
    content: str,
    intent_match: float,
    novelty: float,
    recency: float,
) -> float:
    """
    All inputs must be between 0 and 1
    """
    importance = (
        0.5 * intent_match +
        0.3 * novelty +
        0.2 * recency
    )

    return round(min(max(importance, 0.0), 1.0), 3)


