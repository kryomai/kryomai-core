from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .compute_type import ComputeType


@dataclass
class ComputeDevice:
    name: str
    device_type: ComputeType
    capabilities: list[str] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    available: bool = True