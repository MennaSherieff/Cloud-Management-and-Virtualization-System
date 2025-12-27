import os
import sys

def validate_inputs(cpu, memory, disk_size):
    """
    Validate CPU, memory, and disk size inputs
    """
    try:
        cpu = int(cpu)
        memory = int(memory)

        if cpu < 1:
            raise ValueError("CPU must be at least 1")

        if memory < 256:
            raise ValueError("Memory must be at least 256 MB")

        if not disk_size.endswith("G"):
            raise ValueError("Disk size must end with 'G' (example: 10G)")

        return cpu, memory

    except ValueError as error:
        print(f"❌ Validation Error: {error}")
        sys.exit(1)


def create_disk(disk_name, disk_size):
    """
    Create a QCOW2 disk image if it does not exist
    """
    if not os.path.exists(disk_name):
        print(f"📀 Creating disk image ({disk_size})...")
        result = os.system(f"qemu-img create -f qcow2 {disk_name} {disk_size}")

        if result != 0:
            print("❌ Failed to create disk image.")
            sys.exit(1)
    else:
        print("ℹ️ Disk image already exists.")


def start_vm(cpu, memory, disk_name):
    """
    Start a virtual machine using QEMU
    """
    qemu_cmd = (
        f"qemu-system-x86_64 "
        f"-m {memory} "
        f"-smp {cpu} "
        f"-hda {disk_name} "
        f"-nographic"
    )

    print(f"🚀 Starting VM with {cpu} CPU(s) and {memory}MB RAM...")
    result = os.system(qemu_cmd)

    if result != 0:
        print("❌ Failed to start VM. Please check QEMU installation.")
        sys.exit(1)
