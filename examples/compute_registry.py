from kryomai.compute import ComputeRegistry
from kryomai.core import ComputeDevice


def main():
    registry = ComputeRegistry()

    cpu = ComputeDevice(
        name="System CPU",
        device_type="CPU",
        capabilities=[
            "general_computation",
            "data_processing",
        ],
    )

    gpu = ComputeDevice(
        name="System GPU",
        device_type="GPU",
        capabilities=[
            "parallel_computation",
            "machine_learning",
            "tensor_computation",
        ],
    )

    registry.register(cpu)
    registry.register(gpu)

    print("=== KryomAI Compute Registry ===")

    for device in registry.list_devices():
        print(f"\nDevice: {device.name}")
        print(f"Type: {device.device_type}")
        print(f"Available: {device.available}")
        print("Capabilities:")

        for capability in device.capabilities:
            print(f"  - {capability}")

    print("\n=== Machine Learning Capable Devices ===")

    ml_devices = registry.find_by_capability(
        "machine_learning"
    )

    for device in ml_devices:
        print(f"- {device.name} ({device.device_type})")


if __name__ == "__main__":
    main()