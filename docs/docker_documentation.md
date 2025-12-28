# Docker Command Utility Documentation

## Overview
This utility provides command-line functions for managing Docker containers and images, including creating Dockerfiles, building images, listing images, searching local images, searching DockerHub, and pulling images.

## Functions

### 1. `create_dockerfile()`
Creates a Dockerfile in a specified directory.

#### Inputs:
- **Directory Path:** User is prompted to enter a directory path where the Dockerfile should be saved.
- **Dockerfile Content:** User can repeatedly input lines of text to be included in the Dockerfile. Type `END` on a new line to finish inputting content.

#### Outputs:
- **Success Message:** Prints the path where the Dockerfile was created.
- **Error Message:** Prints if the provided directory path is invalid or if the Dockerfile creation fails.

---

### 2. `build_image(dockerfile_path, image_name)`
Builds a Docker image from the specified Dockerfile.

#### Inputs:
- **dockerfile_path**: String representing the path to the Dockerfile.
- **image_name**: String representing the name and optionally a tag for the image (e.g., `myapp:latest`).

#### Outputs:
- **Command Execution:** Runs the Docker command to build the image.
- **Error Handling:** Prints an error if the command fails.

---

### 3. `list_images()`
Lists all Docker images available locally.

#### Inputs:
- None

#### Outputs:
- **Image List:** Prints the list of local Docker images.
- **Error Message:** Prints if there's a failure in the command execution.

---

### 4. `search_local_images()`
Searches for local Docker images based on user input.

#### Inputs:
- **Search Query:** User is prompted to enter an image name or tag to search for.

#### Outputs:
- **Matched Images:** Prints lines of matching images found locally.
- **No Matches Message:** Prints a message if no matching images are found.
- **Error Message:** Prints if the search command fails.

---

### 5. `search_dockerhub()`
Searches for images on DockerHub based on user input.

#### Inputs:
- **Image Name:** User is prompted to enter an image name to search for on DockerHub.

#### Outputs:
- **DockerHub Search Results:** Runs the search command in the terminal and outputs to the user.
- **Error Message:** Prints if the search command fails.

---

### 6. `pull_image()`
Pulls a Docker image from the DockerHub.

#### Inputs:
- **Image Name:** User is prompted to enter the name of the image to pull (e.g., `ubuntu:latest`).

#### Outputs:
- **Success Message:** Prints a message indicating the image was successfully pulled.
- **Error Message:** Prints if the pull command fails.

---

### 7. list_running_containers()
Lists all currently running Docker containers.

#### Inputs:
- None

#### Outputs:
- **Running Containers:** Displays a table of currently running containers with their details.
- **Error Handling:**
  - If Docker is not installed, raises `FileNotFoundError`
  - If Docker command fails, raises `RuntimeError`


---

### 8. stop_container(container_id)
Stops a running Docker container.

#### Inputs:
- **Container ID/Name:** The ID or name of the container to stop

#### Outputs:
- **Success Message:** Confirmation that the container was stopped
- **Error Handling:**
  - If Docker is not installed, raises `FileNotFoundError`
  - If container ID is empty, raises `ValueError`
  - If container doesn't exist or is not running, raises `RuntimeError`
