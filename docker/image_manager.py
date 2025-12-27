import os              #file/path operations
import subprocess      #running external commands (like Docker CLI)

def build_image(dockerfile_path, image_name):
    #Lab Syntax: docker build -t <image-name>:<tag>

    build_context = os.path.dirname(dockerfile_path)

    command = [
        "docker", "build",
        "-t", image_name,
        "-f", dockerfile_path,
        build_context
    ]

    print("Running:", " ".join(command))

    subprocess.run(command, check=True)           #subprocess.run(): Executes the command



def list_images():
    #Lab Syntax: docker image ls

    print("\nLocal Docker Images")

    try:
        subprocess.run(["docker", "image", "ls"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to list images.")

def search_local_images():
    #Lab Syntax: 

    print("\nSearch Local Docker Images")

    query = input("Enter image name or tag to search: ").strip()

    try:
        result = subprocess.run(
            ["docker", "images"],
            capture_output=True,      #Captures command output instead of printing to terminal
            text=True,                #Returns output as string (not bytes)
            check=True
        )

        matches = [line for line in result.stdout.splitlines() if query in line]   #result.stdout.splitlines(): Splits command output into list of lines


        if matches:
            print("\n".join(matches))
        else:
            print("No matching images found.")
    except subprocess.CalledProcessError:
        print("Error searching images.")

def search_dockerhub():
    #Lab Syntax: docker search <image-name>

    print("\nSearch DockerHub")

    image_name = input("Enter image name to search on DockerHub: ").strip()

    try:
        subprocess.run(
            ["docker", "search", image_name],
            check=True
        )
    except subprocess.CalledProcessError:
        print("DockerHub search failed.")

def pull_image():
    #Syntax: docker pull <image-name>

    print("\nPull Docker Image")

    image_name = input("Enter image name (e.g., ubuntu:latest): ").strip()

    try:
        subprocess.run(
            ["docker", "pull", image_name],
            check=True
        )
        print(f"Image '{image_name}' pulled successfully.")
    except subprocess.CalledProcessError:
        print("Failed to pull image.")


if __name__ == "__main__":
    print("1. Build Image")
    print("2. List Images")
    print("3. Search Local Images")
    print("4. Search DockerHub")
    print("5. Pull Image")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        dockerfile_path = input("Enter path to Dockerfile: ").strip()
        image_name = input("Enter image name and tag (e.g., myapp:latest): ").strip()
        build_image(dockerfile_path, image_name)

    elif choice == "2":
        list_images()
    elif choice == "3":
        search_local_images()
    elif choice == "4":
        search_dockerhub()
    elif choice == "5":
        pull_image()
    else:
        print("Invalid choice.")