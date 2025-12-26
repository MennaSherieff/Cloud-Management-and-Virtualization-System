import os
import subprocess

def build_image():
    print("\nBuild Docker Image")

    dockerfile_path = input("Enter path to Dockerfile: ").strip()
    image_tag = input("Enter image name and tag (e.g., myapp:latest): ").strip()

    try:
        subprocess.run(
            ["docker", "build", "-t", image_tag, "-f", dockerfile_path, "."],
            check=True
        )
        print(f"Image '{image_tag}' built successfully.")
    except subprocess.CalledProcessError:
        print("Failed to build Docker image.")


def list_images():
    print("\nLocal Docker Images")

    try:
        subprocess.run(["docker", "image", "ls"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to list images.")


if __name__ == "__main__":
    build_image()