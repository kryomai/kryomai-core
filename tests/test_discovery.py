from kryomai.compute.discovery import HardwareDiscovery
from kryomai.compute.registry import ComputeRegistry
from kryomai.core.device import ComputeDevice


def test_discover_cpu():
    discovery = HardwareDiscovery()

    cpu = discovery.discover_cpu()

    assert isinstance(cpu, ComputeDevice)
    assert cpu.device_type == "CPU"
    assert cpu.name
    assert "general_computation" in cpu.capabilities


def test_discover_gpu():
    discovery = HardwareDiscovery()

    gpus = discovery.discover_gpu()

    assert isinstance(gpus, list)

    for gpu in gpus:
        assert isinstance(gpu, ComputeDevice)
        assert gpu.device_type == "GPU"
        assert gpu.name
        assert "parallel_computation" in gpu.capabilities


def test_discover_all_hardware():
    discovery = HardwareDiscovery()

    devices = discovery.discover()

    assert isinstance(devices, list)
    assert len(devices) >= 1

    cpu_devices = [
        device for device in devices
        if device.device_type == "CPU"
    ]

    assert len(cpu_devices) >= 1

    for device in devices:
        assert isinstance(device, ComputeDevice)
        assert device.name
        assert device.device_type


def test_discover_and_register():
    discovery = HardwareDiscovery()
    registry = ComputeRegistry()

    discovery.discover_and_register(registry)

    devices = registry.list_devices()

    assert len(devices) >= 1

    cpu_devices = [
        device
        for device in devices
        if device.device_type == "CPU"
    ]

    assert len(cpu_devices) >= 1