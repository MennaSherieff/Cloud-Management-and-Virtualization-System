import subprocess
import os


def build_image(dockerfile_path, image_name):
    """
    Build a Docker image from a Dockerfile.

    Args:
        dockerfile_path: Path to the Dockerfile
        image_name: Name/tag for the Docker image

    Returns:
        str: Success message after building the image

    Raises:
        ValueError: If Dockerfile path or image name is invalid
        FileNotFoundError: If the Dockerfile does not exist
        subprocess.CalledProcessError: If Docker build fails
        PermissionError: If access to the path is denied
    """
    if not dockerfile_path or not image_name:
        raise ValueError("Dockerfile path and image name are required.")

    if not os.path.isfile(dockerfile_path):
        raise FileNotFoundError("Dockerfile not found.")

    try:
        build_context = os.path.dirname(dockerfile_path)
        command = ["docker", "build", "-t", image_name, "-f", dockerfile_path, build_context]
        subprocess.run(command, check=True)
        return f"Image '{image_name}' built successfully."
    except PermissionError:
        raise PermissionError("Permission denied while accessing Dockerfile.")
    except subprocess.CalledProcessError:
        raise subprocess.CalledProcessError(1, "Docker build failed.")


def list_images():
    """
    List all local Docker images.

    Returns:
        str: Output of Docker images list

    Raises:
        RuntimeError: If Docker is not running
        subprocess.CalledProcessError: If Docker command fails
        FileNotFoundError: If Docker is not installed
    """
    try:
        result = subprocess.run(
            ["docker", "image", "ls"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except FileNotFoundError:
        raise FileNotFoundError("Docker is not installed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to list Docker images.")


def search_local_images(query):
    """
    Search local Docker images by keyword.

    Args:
        query: Search keyword

    Returns:
        str: Matching images or a not-found message

    Raises:
        ValueError: If query is empty
        subprocess.CalledProcessError: If Docker command fails
        FileNotFoundError: If Docker is not installed
    """
    if not query:
        raise ValueError("Search query cannot be empty.")

    try:
        result = subprocess.run(
            ["docker", "images"],
            capture_output=True,
            text=True,
            check=True
        )
        matches = [line for line in result.stdout.splitlines() if query in line]
        return "\n".join(matches) if matches else "No matching images found."
    except FileNotFoundError:
        raise FileNotFoundError("Docker is not installed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to search local Docker images.")


def search_dockerhub(query):
    """
    Search Docker Hub for images.

    Args:
        query: Search keyword

    Returns:
        str: Search results from Docker Hub

    Raises:
        ValueError: If query is empty
        subprocess.CalledProcessError: If Docker search fails
        FileNotFoundError: If Docker is not installed
    """
    if not query:
        raise ValueError("Search query cannot be empty.")

    try:
        result = subprocess.run(
            ["docker", "search", query],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except FileNotFoundError:
        raise FileNotFoundError("Docker is not installed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("Docker Hub search failed.")


def pull_image(image_name):
    """
    Pull a Docker image from Docker Hub.

    Args:
        image_name: Name of the Docker image

    Returns:
        str: Success message after pulling the image

    Raises:
        ValueError: If image name is empty
        subprocess.CalledProcessError: If pull fails
        FileNotFoundError: If Docker is not installed
        RuntimeError: If image does not exist
    """
    if not image_name:
        raise ValueError("Image name cannot be empty.")

    try:
        subprocess.run(["docker", "pull", image_name], check=True)
        return f"Image '{image_name}' pulled successfully."
    except FileNotFoundError:
        raise FileNotFoundError("Docker is not installed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to pull the image.")