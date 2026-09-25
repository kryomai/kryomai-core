"""Example: KryomAI hardware discovery."""

from kryomai.compute.discovery import HardwareDiscovery


def main() -> None:
    """Discover and display available hardware."""

    discovery = HardwareDiscovery()
    devices = discovery.discover()

    print()
    print("KryomAI Hardware Discovery")
    print("=" * 30)

    for device in devices:
        print()
        print(f"Name: {device.name}")
        print(f"Type: {device.device_type}")
        print(f"Capabilities: {', '.join(device.capabilities)}")
        print(f"Available: {device.available}")


if __name__ == "__main__":
    main()
