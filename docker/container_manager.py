import subprocess


def list_running_containers():
    """
    List all currently running Docker containers.

    Returns:
        str: Output of running Docker containers

    Raises:
        RuntimeError: If Docker is not running
        subprocess.CalledProcessError: If Docker command fails
        FileNotFoundError: If Docker is not installed
    """
    try:
        result = subprocess.run(
            ["docker", "ps"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except FileNotFoundError:
        raise FileNotFoundError("Docker is not installed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to list running containers.")


def stop_container(container_id):
    """
    Stop a running Docker container.

    Args:
        container_id: ID or name of the container to stop

    Returns:
        str: Success message after stopping the container

    Raises:
        ValueError: If container ID is empty
        subprocess.CalledProcessError: If stopping the container fails
        FileNotFoundError: If Docker is not installed
        RuntimeError: If container does not exist or is not running
    """
    if not container_id:
        raise ValueError("Container ID cannot be empty.")

    try:
        subprocess.run(["docker", "stop", container_id], check=True)
        return f"Container '{container_id}' stopped successfully."
    except FileNotFoundError:
        raise FileNotFoundError("Docker is not installed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to stop container. Check if it exists and is running.")
