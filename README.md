# Cloud Management and Virtualization System

### Course: Cloud Computing and Networking  
**Instructor:** Dr. Mohamed ElGazzar  
---

## Project Overview

The **Cloud Management System** is a command-line based application designed to manage **Virtual Machines (VMs)** using **QEMU** and **containerized environments** using **Docker**.  
The system provides users with a unified interface to perform virtualization and container management tasks based on user input or configuration files.

This project aims to enhance practical understanding of:
- Virtualization technologies
- VM lifecycle management
- Docker image and container operations
- System-level automation

---

## Project Objectives

The main objectives of this project are to:

- Automate **virtual machine creation** using QEMU
- Allow VM configuration via:
  - Interactive user input
  - Configuration files
- Enable **Dockerfile creation**
- Build, list, search, and download **Docker images**
- Manage **Docker containers**
- Provide a **user-friendly CLI interface**
- Apply best practices in code organization and documentation

---

## Technologies Used

- **Programming Language:** Python
- **Virtualization:** QEMU
- **Containerization:** Docker
- **Interface:** Command-Line Interface (CLI)
---

## System Features

### 🔹 Virtual Machine Management (QEMU)
- Create virtual machines with custom:
  - CPU cores
  - Memory size
  - Disk size
  - OS ISO image
- Support for configuration files (JSON)

### 🔹 Dockerfile Management
- Create Dockerfiles using user-provided content
- Specify custom save paths

### 🔹 Docker Image Management
- Build Docker images
- List all local Docker images
- Search for local images
- Search for images on DockerHub
- Pull/download images from DockerHub

### 🔹 Docker Container Management
- List all running containers
- Stop a container using container ID or name

---

## Project Structure

```text
cloud-management-system/
├── vm/            # vm source code
├── docker/        # docker source code
├── docs/           # User manual & reports
├── README.md
├── main.py
