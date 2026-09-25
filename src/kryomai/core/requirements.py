from dataclasses import dataclass, field

from .compute_type import ComputeType


@dataclass(frozen=True)
class CapabilityRequirement:
    """
    Describes a capability required or preferred by a task.
    """

    name: str
    required: bool = True

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Capability name cannot be empty.")

        if not isinstance(self.required, bool):
            raise TypeError("required must be a boolean.")


@dataclass(frozen=True)
class ResourceRequirements:
    """
    Describes the compute resources required by a task.

    These fields are intentionally optional because different
    compute backends expose different resource models.
    """

    cpu_cores: int | None = None
    memory_mb: int | None = None
    gpu_memory_mb: int | None = None

    def __post_init__(self) -> None:
        if self.cpu_cores is not None and self.cpu_cores <= 0:
            raise ValueError("cpu_cores must be greater than zero.")

        if self.memory_mb is not None and self.memory_mb <= 0:
            raise ValueError("memory_mb must be greater than zero.")

        if self.gpu_memory_mb is not None and self.gpu_memory_mb <= 0:
            raise ValueError("gpu_memory_mb must be greater than zero.")


@dataclass
class TaskRequirements:
    """
    Defines the requirements and preferences used to determine
    which compute device can execute a task.

    The requirements layer is intentionally independent of the
    scheduler, matcher, runtime, and backend implementations.
    """

    capabilities: list[CapabilityRequirement] = field(
        default_factory=list
    )

    preferred_device_types: list[ComputeType] = field(
        default_factory=list
    )

    resources: ResourceRequirements = field(
        default_factory=ResourceRequirements
    )

    priority: int = 0

    def __post_init__(self) -> None:
        if any(
            not isinstance(device_type, ComputeType)
            for device_type in self.preferred_device_types
        ):
            raise TypeError(
                "preferred_device_types must contain only ComputeType values."
            )

        if not isinstance(self.priority, int):
            raise TypeError("priority must be an integer.")