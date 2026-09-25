from kryomai.compute.registry import ComputeRegistry
from kryomai.core import ComputeDevice


def test_register_device():
    registry = ComputeRegistry()

    cpu = ComputeDevice(
        name="System CPU",
        device_type="CPU",
    )

    registry.register(cpu)

    devices = registry.list_devices()

    assert len(devices) == 1
    assert devices[0].name == "System CPU"
    assert devices[0].device_type == "CPU"


def test_register_multiple_devices():
    registry = ComputeRegistry()

    cpu = ComputeDevice(
        name="System CPU",
        device_type="CPU",
    )

    gpu = ComputeDevice(
        name="System GPU",
        device_type="GPU",
    )

    registry.register(cpu)
    registry.register(gpu)

    devices = registry.list_devices()

    assert len(devices) == 2


def test_find_devices_by_capability():
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
        ],
    )

    registry.register(cpu)
    registry.register(gpu)

    devices = registry.find_by_capability("machine_learning")

    assert len(devices) == 1
    assert devices[0].device_type == "GPU"