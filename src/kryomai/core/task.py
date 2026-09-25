from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from .requirements import TaskRequirements


@dataclass
class Task:
    name: str
    description: str
    requirements: TaskRequirements = field(
        default_factory=TaskRequirements
    )
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))