from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .execution import Execution


@dataclass
class ExecutionResult:
    execution: Execution
    success: bool
    data: object = None
    error: str | None = None
    id: UUID = field(default_factory=uuid4)