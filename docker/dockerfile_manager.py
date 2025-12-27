import os

def create_dockerfile():
    print("Dockerfile Creation")

    path = input("Enter directory path to save Dockerfile: ").strip()

    if not os.path.isdir(path):
        print("Invalid directory path.")
        return

    print("Enter Dockerfile content (type 'END' on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    dockerfile_path = os.path.join(path, "Dockerfile")

    try:
        with open(dockerfile_path, "w") as f:
            f.write("\n".join(lines))
        print(f"Dockerfile created at: {dockerfile_path}")
    except Exception as e:
        print(f"Failed to create Dockerfile: {e}")

if __name__ == "__main__":
    create_dockerfile()