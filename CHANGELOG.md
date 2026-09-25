# Changelog

All notable changes to KryomAI Core are documented here.


## [0.2.0] - Task Requirements & Compute Type Foundation

### Added

- Added `ComputeType` enumeration for heterogeneous compute categories.
- Added `TaskRequirements` for describing task-level compute requirements.
- Added `CapabilityRequirement` for required and optional capabilities.
- Added `ResourceRequirements` for CPU, system memory, and GPU memory requirements.
- Added validation for capability names.
- Added validation for resource requirements.
- Added validation for preferred compute device types.
- Added validation for task priority.
- Added comprehensive requirements test coverage.

### Changed

- Updated `ComputeDevice.device_type` to use `ComputeType`.
- Updated hardware discovery to use typed compute categories.
- Updated `Task` to include `TaskRequirements`.
- Updated core exports for new requirements and compute type abstractions.

### Architecture

Introduced the first structured task-requirements layer for future compute matching and heterogeneous compute orchestration.

The requirements architecture now provides the foundation for:

- Capability-aware compute matching
- Compute-type preferences
- Resource-aware scheduling
- Future heterogeneous compute selection
- Future CPU, GPU, NPU, FPGA, QPU, HPU, HPC, and robotics backends

### Validation

- Ruff: all checks passed
- Pytest: 44 tests passed


## [0.1.5] - Foundation Cleanup & Engineering Hardening

### Added

- Standardized project version to `0.1.5`
- Added Ruff configuration for code quality and import ordering
- Added pytest configuration
- Added development dependencies
- Improved project metadata and development tooling configuration

### Changed

- Cleaned and standardized Python imports
- Removed unused imports
- Standardized `__all__` ordering
- Improved development configuration in `pyproject.toml`

### Engineering

- Established Ruff as the code-quality baseline
- Established automated pytest regression testing
- Confirmed all existing tests pass after code-quality changes

### Validation

- Ruff: all checks passed
- Pytest: 9 tests passed

---

## [0.1.4] - Compute Capabilities

### Added

- Added capability support to `ComputeDevice`
- Added capability-based device discovery
- Added `ComputeRegistry.find_by_capability()`
- Added tests for capability matching
- Updated compute registry example

### Architecture

Introduced the foundational domain concept of compute capabilities.

A compute device can now expose capabilities that describe the types of computation it supports.

Example capabilities include:

- `general_computation`
- `data_processing`
- `parallel_computation`
- `machine_learning`
- `tensor_computation`

This establishes the foundation for future capability-aware compute selection.

---

## [0.1.3]

### Added

- Initial compute registry functionality
- Device registration
- Device lookup
- Device listing
- Device removal

---

## [0.1.2]

### Added

- Execution model
- Execution result model
- Task and device relationships

---

## [0.1.1]

### Added

- Core task model
- Compute device model
- Initial project structure

---

## [0.1.0]

### Added

- Initial KryomAI Core foundation
- Python package structure
- Basic project metadata