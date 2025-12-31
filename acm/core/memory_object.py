from datetime import datetime
from pydantic import BaseModel
import uuid
from typing import List

class MemoryObject(BaseModel):
    id: str
    content: str
    importance: float
    embedding: List[float]
    created_at: datetime

    @staticmethod
    def create(content: str, importance: float, embedding: list):
        return MemoryObject(
            id=str(uuid.uuid4()),
            content=content,
            importance=importance,
            embedding=embedding,
            created_at=datetime.utcnow()
        )

