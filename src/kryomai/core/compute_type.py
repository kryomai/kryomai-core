from enum import StrEnum


class ComputeType(StrEnum):
    CPU = "CPU"
    GPU = "GPU"
    NPU = "NPU"
    FPGA = "FPGA"
    QPU = "QPU"
    HPU = "HPU"
    HPC = "HPC"
    ROBOTICS = "ROBOTICS"

    