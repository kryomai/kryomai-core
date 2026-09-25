from kryomai.core import ComputeDevice


class ComputeRegistry:
    def __init__(self):
        self._devices: dict[str, ComputeDevice] = {}

    def register(self, device: ComputeDevice) -> None:
        self._devices[str(device.id)] = device

    def get(self, device_id: str) -> ComputeDevice | None:
        return self._devices.get(device_id)

    def list_devices(self) -> list[ComputeDevice]:
        return list(self._devices.values())

    def remove(self, device_id: str) -> None:
        self._devices.pop(device_id, None)

    def find_by_capability(
    self,
    capability: str,
) -> list[ComputeDevice]:
        
        return [
           device
           for device in self._devices.values()
           if capability in device.capabilities
        ]