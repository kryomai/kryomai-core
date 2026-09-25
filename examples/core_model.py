from kryomai.core import (
    Task,
    ComputeCapability,
    ComputeDevice,
    Execution,
    ExecutionResult,
)


def main():
    task = Task(
        name="Dataset Analysis",
        description="Analyze a machine learning dataset",
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

    print("=== KryomAI Core Model ===")
    print(f"Task: {task.name}")
    print(f"Capability: {capability.name}")
    print(f"Device: {device.name}")
    print(f"Device Type: {device.device_type}")
    print(f"Execution Status: {execution.status}")
    print(f"Success: {result.success}")
    print(f"Result: {result.data}")


if __name__ == "__main__":
    main()