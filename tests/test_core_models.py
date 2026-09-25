from kryomai.core import (
    CapabilityRequirement,
    ComputeCapability,
    ComputeDevice,
    ComputeType,
    Execution,
    ExecutionResult,
    Task,
    TaskRequirements,
)


def test_core_system_model():
    task = Task(
        name="Dataset Analysis",
        description="Analyze a dataset",
    )

    capability = ComputeCapability(
        name="data_processing",
        description="General-purpose data processing",
    )

    device = ComputeDevice(
        name="System CPU",
        device_type="CPU",
    )

    execution = Execution(
        task=task,
        device=device,
    )

    result = ExecutionResult(
        execution=execution,
        success=True,
        data="Analysis completed",
    )

    assert task.name == "Dataset Analysis"
    assert capability.name == "data_processing"
    assert device.device_type == "CPU"
    assert execution.status == "pending"
    assert result.success is True


def test_task_with_requirements():
    task = Task(
        name="ML Task",
        description="Machine learning workload",
        requirements=TaskRequirements(
            capabilities=[
                CapabilityRequirement("machine_learning"),
            ],
            preferred_device_types=[ComputeType.GPU],
            priority=10,
        ),
    )

    assert task.requirements.priority == 10
    assert task.requirements.preferred_device_types == ["GPU"]
    assert task.requirements.capabilities[0].name == "machine_learning"