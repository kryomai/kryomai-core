from kryomai.core import (
    Task,
    ComputeCapability,
    ComputeDevice,
    Execution,
    ExecutionResult,
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