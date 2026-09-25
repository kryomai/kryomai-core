import pytest

from kryomai.core import (
    CapabilityRequirement,
    ComputeType,
    ResourceRequirements,
    TaskRequirements,
)

# ---------------------------------------------------------------------------
# CapabilityRequirement
# ---------------------------------------------------------------------------


def test_capability_requirement_defaults_to_required():
    requirement = CapabilityRequirement(
        name="machine_learning",
    )

    assert requirement.name == "machine_learning"
    assert requirement.required is True


def test_capability_requirement_can_be_optional():
    requirement = CapabilityRequirement(
        name="tensor_computation",
        required=False,
    )

    assert requirement.name == "tensor_computation"
    assert requirement.required is False


def test_capability_requirement_preserves_name():
    requirement = CapabilityRequirement(
        name="parallel_computation",
    )

    assert requirement.name == "parallel_computation"


def test_empty_capability_name_is_rejected():
    with pytest.raises(ValueError):
        CapabilityRequirement(name="")


def test_whitespace_only_capability_name_is_rejected():
    with pytest.raises(ValueError):
        CapabilityRequirement(name="   ")


def test_invalid_required_value_is_rejected():
    with pytest.raises(TypeError):
        CapabilityRequirement(
            name="tensor_computation",
            required="yes",
        )


def test_capability_requirement_is_immutable():
    requirement = CapabilityRequirement(
        name="machine_learning",
    )

    with pytest.raises(AttributeError):
        requirement.name = "other_capability"


# ---------------------------------------------------------------------------
# ResourceRequirements
# ---------------------------------------------------------------------------


def test_resource_requirements_defaults_to_none():
    resources = ResourceRequirements()

    assert resources.cpu_cores is None
    assert resources.memory_mb is None
    assert resources.gpu_memory_mb is None


def test_resource_requirements():
    resources = ResourceRequirements(
        cpu_cores=4,
        memory_mb=8192,
        gpu_memory_mb=4096,
    )

    assert resources.cpu_cores == 4
    assert resources.memory_mb == 8192
    assert resources.gpu_memory_mb == 4096


def test_resource_requirements_accepts_cpu_cores():
    resources = ResourceRequirements(cpu_cores=8)

    assert resources.cpu_cores == 8


def test_resource_requirements_accepts_memory():
    resources = ResourceRequirements(memory_mb=16384)

    assert resources.memory_mb == 16384


def test_resource_requirements_accepts_gpu_memory():
    resources = ResourceRequirements(gpu_memory_mb=8192)

    assert resources.gpu_memory_mb == 8192


def test_invalid_cpu_cores_are_rejected():
    with pytest.raises(ValueError):
        ResourceRequirements(cpu_cores=0)


def test_negative_cpu_cores_are_rejected():
    with pytest.raises(ValueError):
        ResourceRequirements(cpu_cores=-1)


def test_invalid_memory_is_rejected():
    with pytest.raises(ValueError):
        ResourceRequirements(memory_mb=0)


def test_negative_memory_is_rejected():
    with pytest.raises(ValueError):
        ResourceRequirements(memory_mb=-1024)


def test_invalid_gpu_memory_is_rejected():
    with pytest.raises(ValueError):
        ResourceRequirements(gpu_memory_mb=0)


def test_negative_gpu_memory_is_rejected():
    with pytest.raises(ValueError):
        ResourceRequirements(gpu_memory_mb=-1024)


def test_resource_requirements_are_immutable():
    resources = ResourceRequirements(
        cpu_cores=4,
        memory_mb=8192,
    )

    with pytest.raises(AttributeError):
        resources.cpu_cores = 8


# ---------------------------------------------------------------------------
# TaskRequirements
# ---------------------------------------------------------------------------


def test_task_requirements_defaults():
    requirements = TaskRequirements()

    assert requirements.capabilities == []
    assert requirements.preferred_device_types == []
    assert requirements.resources == ResourceRequirements()
    assert requirements.priority == 0


def test_task_requirements():
    requirements = TaskRequirements(
        capabilities=[
            CapabilityRequirement("machine_learning"),
            CapabilityRequirement("tensor_computation"),
        ],
        preferred_device_types=[ComputeType.GPU],
        resources=ResourceRequirements(
            memory_mb=8192,
            gpu_memory_mb=4096,
        ),
        priority=10,
    )

    assert len(requirements.capabilities) == 2
    assert requirements.preferred_device_types == [ComputeType.GPU]
    assert requirements.resources.memory_mb == 8192
    assert requirements.resources.gpu_memory_mb == 4096
    assert requirements.priority == 10


def test_task_requirements_support_multiple_compute_types():
    requirements = TaskRequirements(
        preferred_device_types=[
            ComputeType.GPU,
            ComputeType.NPU,
        ]
    )

    assert requirements.preferred_device_types == [
        ComputeType.GPU,
        ComputeType.NPU,
    ]


def test_task_requirements_support_all_compute_types():
    requirements = TaskRequirements(
        preferred_device_types=[
            ComputeType.CPU,
            ComputeType.GPU,
            ComputeType.NPU,
            ComputeType.FPGA,
            ComputeType.QPU,
            ComputeType.HPU,
            ComputeType.HPC,
            ComputeType.ROBOTICS,
        ]
    )

    assert len(requirements.preferred_device_types) == 8


def test_invalid_preferred_device_type_is_rejected():
    with pytest.raises(TypeError):
        TaskRequirements(
            preferred_device_types=["GPU"],
        )


def test_mixed_invalid_preferred_device_types_are_rejected():
    with pytest.raises(TypeError):
        TaskRequirements(
            preferred_device_types=[
                ComputeType.GPU,
                "NPU",
            ],
        )


def test_task_requirements_accepts_required_and_optional_capabilities():
    requirements = TaskRequirements(
        capabilities=[
            CapabilityRequirement(
                name="machine_learning",
                required=True,
            ),
            CapabilityRequirement(
                name="tensor_computation",
                required=False,
            ),
        ]
    )

    assert requirements.capabilities[0].required is True
    assert requirements.capabilities[1].required is False


def test_task_requirements_accepts_resource_requirements():
    resources = ResourceRequirements(
        cpu_cores=4,
        memory_mb=8192,
        gpu_memory_mb=4096,
    )

    requirements = TaskRequirements(
        resources=resources,
    )

    assert requirements.resources is resources


def test_task_requirements_accepts_zero_priority():
    requirements = TaskRequirements(priority=0)

    assert requirements.priority == 0


def test_task_requirements_accepts_positive_priority():
    requirements = TaskRequirements(priority=100)

    assert requirements.priority == 100


def test_task_requirements_accepts_negative_priority():
    requirements = TaskRequirements(priority=-10)

    assert requirements.priority == -10


def test_invalid_priority_type_is_rejected():
    with pytest.raises(TypeError):
        TaskRequirements(priority="high")


def test_task_requirements_use_independent_default_capabilities():
    first = TaskRequirements()
    second = TaskRequirements()

    first.capabilities.append(
        CapabilityRequirement("machine_learning")
    )

    assert first.capabilities != second.capabilities
    assert second.capabilities == []


def test_task_requirements_use_independent_default_device_types():
    first = TaskRequirements()
    second = TaskRequirements()

    first.preferred_device_types.append(ComputeType.GPU)

    assert first.preferred_device_types != second.preferred_device_types
    assert second.preferred_device_types == []


def test_task_requirements_use_independent_default_resources():
    first = TaskRequirements()
    second = TaskRequirements()

    first.resources = ResourceRequirements(cpu_cores=4)

    assert first.resources != second.resources
    assert second.resources == ResourceRequirements()