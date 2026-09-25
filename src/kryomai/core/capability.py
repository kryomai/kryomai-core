from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeCapability:
    name: str
    description: str