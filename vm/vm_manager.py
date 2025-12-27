import sys
from utils import validate_inputs, create_disk, start_vm

def interactive_mode():
    """
    Interactive VM creation (Requirement 1a)
    """
    cpu = input("Enter number of CPUs: ")
    memory = input("Enter memory size (MB): ")
    disk_size = input("Enter disk size (e.g., 10G): ")

    cpu, memory = validate_inputs(cpu, memory, disk_size)
    disk_name = "interactive_vm.qcow2"

    create_disk(disk_name, disk_size)
    start_vm(cpu, memory, disk_name)


def config_mode():
    """
    VM creation using configuration file (Requirement 1b)
    """
    config = {}

    try:
        with open("config.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                config[key] = value
    except FileNotFoundError:
        print("❌ config.txt file not found.")
        sys.exit(1)

    cpu, memory = validate_inputs(
        config["cpu"],
        config["memory"],
        config["disk_size"]
    )

    disk_name = "config_vm.qcow2"
    create_disk(disk_name, config["disk_size"])
    start_vm(cpu, memory, disk_name)


# ---------------- MAIN MENU ----------------

print("=== Cloud VM Management System (QEMU) ===")
print("1. Interactive VM Creation")
print("2. VM Creation from Config File")

choice = input("Choose an option: ")

if choice == "1":
    interactive_mode()
elif choice == "2":
    config_mode()
else:
    print("❌ Invalid choice.")
