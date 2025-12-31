from datetime import datetime

def apply_decay(importance: float, created_at: datetime) -> float:
    """
    Exponential decay: memory importance reduces over time
    """
    days_passed = (datetime.utcnow() - created_at).days
    decay_rate = 0.98  # 2% per day

    return round(importance * (decay_rate ** days_passed), 3)
