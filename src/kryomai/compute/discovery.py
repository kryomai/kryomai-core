"""Hardware discovery for KryomAI."""

from __future__ import annotations

import platform
import subprocess

from kryomai.core.device import ComputeDevice
from kryomai.compute.registry import ComputeRegistry


class HardwareDiscovery:
    """Discover hardware devices available on the host system."""

    def discover_cpu(self) -> ComputeDevice:
        """Discover the system CPU."""

        cpu_name = platform.processor()

        if not cpu_name:
            cpu_name = platform.machine()

        return ComputeDevice(
            name=cpu_name,
            device_type="CPU",
            capabilities=[
                "general_computation",
                "data_processing",
            ],
        )

    def discover_gpu(self) -> list[ComputeDevice]:
        """Discover GPUs available on the system."""

        devices: list[ComputeDevice] = []

        try:
            result = subprocess.run(
                [
                    "wmic",
                    "path",
                    "win32_VideoController",
                    "get",
                    "Name",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode != 0:
                return devices

            for line in result.stdout.splitlines():
                name = line.strip()

                if not name or name.lower() == "name":
                    continue

                devices.append(
                    ComputeDevice(
                        name=name,
                        device_type="GPU",
                        capabilities=[
                            "parallel_computation",
                            "machine_learning",
                            "tensor_computation",
                        ],
                    )
                )

        except (FileNotFoundError, OSError):
            return devices

        return devices

    def discover(self) -> list[ComputeDevice]:
        """Discover all supported hardware devices."""

        devices: list[ComputeDevice] = []

        devices.append(self.discover_cpu())
        devices.extend(self.discover_gpu())

        return devices

    def discover_and_register(
        self,
        registry: ComputeRegistry,
    ) -> ComputeRegistry:
        """Discover hardware and register devices."""

        devices = self.discover()

        for device in devices:
            registry.register(device)

        return registry