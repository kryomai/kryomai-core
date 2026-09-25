# Changelog

## [0.1.3] - Compute Capabilities

### Added

- Added capability support to `ComputeDevice`
- Added capability-based device discovery
- Added `ComputeRegistry.find_by_capability()`
- Added tests for capability matching
- Updated compute registry example

### Architecture

Introduced the foundational domain model for:

Task → Capability → Compute Device → Execution → Result