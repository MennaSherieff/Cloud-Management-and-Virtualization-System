import subprocess

def list_running_containers():
    print("\n=== Running Containers ===")
    subprocess.run(["docker", "ps"])

def list_all_containers():
    print("\n=== All Containers ===")
    subprocess.run(["docker", "ps", "-a"])

def stop_container():
    container_id = input("Enter the container ID or name to stop: ")
    subprocess.run(["docker", "stop", container_id])

def delete_container():
    container_id = input("Enter the container ID or name to delete: ")
    subprocess.run(["docker", "rm", container_id])

def main():
    while True:
        print("\nDocker Container Management")
        print("1. List running containers")
        print("2. List all containers")
        print("3. Stop a container")
        print("4. Delete a container")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_running_containers()
        elif choice == "2":
            list_all_containers()
        elif choice == "3":
            stop_container()
        elif choice == "4":
            delete_container()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()

# Testcase for Docker commands
# docker pull hello-world
# docker run hello-world

# docker pull alpine
# docker run -it alpine sh

# docker pull nginx
# docker run -d -p 8080:80 nginx

# docker pull redis
# docker run -d --name test-redis redis

