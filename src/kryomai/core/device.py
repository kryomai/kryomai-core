from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class ComputeDevice:
    name: str
    device_type: str
    id: UUID = field(default_factory=uuid4)
    available: bool = True