from dataclasses import dataclass

@dataclass
class ContextConfig:
    # Token management
    max_prompt_tokens: int = 8000
    max_memory_tokens: int = 4000

    # Short-term memory
    short_term_limit: int = 10

    # Summarization
    summarize_after_steps: int = 5
    summary_max_tokens: int = 512

    # Memory scoring
    importance_threshold: float = 0.5
    decay_rate: float = 0.01

    # Safety / learning
    enable_learning: bool = True


