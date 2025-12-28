from vm.utils import validate_inputs, create_disk, start_vm

def interactive_mode(cpu, memory, disk_size):
    """
    Create a VM interactively by passing CPU, memory, and disk_size as arguments.
    """
    cpu, memory = validate_inputs(cpu, memory, disk_size)
    disk_name = "interactive_vm.qcow2"
    create_disk(disk_name, disk_size)
    start_vm(cpu, memory, disk_name)

def config_mode():
    """
    Create VM from config.txt (no input prompts)
    """
    config = {}
    try:
        with open("vm/config.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                config[key] = value
    except FileNotFoundError:
        raise FileNotFoundError("config.txt not found in vm/ folder.")

    cpu, memory = validate_inputs(config["cpu"], config["memory"], config["disk_size"])
    disk_name = "config_vm.qcow2"
    create_disk(disk_name, config["disk_size"])
    start_vm(cpu, memory, disk_name)
