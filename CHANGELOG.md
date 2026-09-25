Changelog
[0.1.4] - Hardware Discovery
Added
Added HardwareDiscovery for automatic hardware detection.
Added CPU discovery.
Added GPU discovery for Windows systems.
Added automatic conversion of discovered hardware into ComputeDevice objects.
Added hardware discovery integration with ComputeRegistry.
Added discover_and_register() for automatic device registration.
Added hardware discovery tests.
Added registry integration tests.
Added hardware discovery example.
Architecture
Introduced the hardware discovery layer:
Hardware
↓
Hardware Discovery
↓
ComputeDevice
↓
Compute Registry
Verification
9 tests passing.
CPU successfully detected on Windows.
GPU discovery gracefully handles systems without a GPU.
