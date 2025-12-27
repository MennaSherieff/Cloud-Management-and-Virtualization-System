# Cloud Management System

A command-line based **Cloud Management System** that automates **virtual machine creation using QEMU** and **container/image management using Docker**.  
The system provides a unified interface for managing virtualization resources through simple user interactions.

---

## Overview

Managing virtual machines and Docker resources often requires working with multiple commands and tools.  
This project simplifies that process by offering a **single CLI-based management layer** that allows users to:

- Create and configure virtual machines
- Generate Dockerfiles
- Build, search, and pull Docker images
- Monitor and control running Docker containers

---

## Key Features

### Virtual Machine Management (QEMU)
- Create virtual machines with custom:
  - CPU cores
  - Memory size
  - Disk size
  - OS ISO image
- Support for configuration files (JSON)

### Dockerfile Management
- Create Dockerfiles with user-defined content
- Specify custom file paths

### Docker Image Management
- Build Docker images
- List available local images
- Search for images locally
- Search for images on DockerHub
- Pull/download images from DockerHub

### Docker Container Management
- List all running containers
- Stop containers by ID or name

---

## Tech Stack

- **Language:** Python 3
- **Virtualization:** QEMU
- **Containerization:** Docker
- **Interface:** Command-Line Interface (CLI)

---

## Project Structure

```text
cloud-management-system/
├── vm/            # vm source code
├── docker/        # docker source code
│   ├── dockerfile_manager.py
│   ├── image_manager.py
│   ├── container_manager.py
├── docs/           # Documentation & reports
│   ├── docker_documentation.md
├── README.md
├── main.py
