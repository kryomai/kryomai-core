from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass
class Task:
    name: str
    description: str
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )