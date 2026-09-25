from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from .device import ComputeDevice
from .task import Task


@dataclass
class Execution:
    task: Task
    device: ComputeDevice
    id: UUID = field(default_factory=uuid4)
    status: str = "pending"
    started_at: datetime | None = None
    completed_at: datetime | None = None