import streamlit as st
from vm.vm_manager import interactive_mode, config_mode
from docker.dockerfile_manager import create_dockerfile
from docker.image_manager import build_image, list_images, search_local_images, search_dockerhub, pull_image
from docker.container_manager import list_running_containers, stop_container

# -------------------- UI --------------------
st.title("☁ Cloud Management System")

# Sidebar with dropdown menus
st.sidebar.title("☁ Navigation")

# Create a session state to track the selected menu
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = None

# VM Dropdown
with st.sidebar.expander("🖥️ VM"):
    if st.button("Create VM (QEMU)"):
        st.session_state.selected_menu = "Create VM (QEMU)"
    if st.button("Create VM from Config File"):
        st.session_state.selected_menu = "Create VM from Config File"

# Docker Dropdown
with st.sidebar.expander("🐳 Docker"):
    if st.button("📝 Create Dockerfile"):
        st.session_state.selected_menu = "Create Dockerfile"
    if st.button("🛠️ Build Docker Image"):
        st.session_state.selected_menu = "Build Docker Image"
    if st.button("📦 List Local Docker Images"):
        st.session_state.selected_menu = "List Local Docker Images"
    if st.button("🔍 Search Local Docker Image"):
        st.session_state.selected_menu = "Search Local Docker Image"
    if st.button("🌐 Search Image on DockerHub"):
        st.session_state.selected_menu = "Search Image on DockerHub"
    if st.button("⬇️ Pull Docker Image"):
        st.session_state.selected_menu = "Pull Docker Image"
    if st.button("📋 List Running Containers"):
        st.session_state.selected_menu = "List Running Containers"
    if st.button("⏹️ Stop Container"):
        st.session_state.selected_menu = "Stop Container"

# Set the selected menu
menu = st.session_state.selected_menu

# -------------------- VM --------------------

if menu == "Create VM (QEMU)":
    st.header("Interactive VM Creation")
    cpu = st.number_input("CPU cores", min_value=1, max_value=16, value=2)
    memory = st.number_input("Memory (MB)", min_value=256, max_value=32768, value=2048)
    disk_size = st.text_input("Disk Size (e.g., 10G)", value="10G")
    if st.button("Create VM"):
        try:
            interactive_mode(cpu, memory, disk_size)
            st.success("VM started successfully!")
        except Exception as e:
            st.error(f"VM creation failed: {e}")

elif menu == "Create VM from Config File" or menu == "Create VM from Config File":
    st.header("VM Creation from config.txt")
    if st.button("Create VM from Config"):
        try:
            config_mode()
            st.success("VM created from config.txt successfully!")
        except Exception as e:
            st.error(f"VM creation failed: {e}")

# -------------------- Dockerfile --------------------
elif menu == "Create Dockerfile" or menu == "📝 Create Dockerfile":
    st.header("Create Dockerfile")
    path = st.text_input("Directory path to save Dockerfile")
    content = st.text_area("Dockerfile content (lines separated by newline)")
    if st.button("Create Dockerfile"):
        try:
            lines = content.strip().split("\n")
            msg = create_dockerfile(path, lines)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

# -------------------- Docker Images --------------------
elif menu == "Build Docker Image" or menu == "🛠️ Build Docker Image":
    st.header("Build Docker Image")
    dockerfile_path = st.text_input("Dockerfile Path")
    image_name = st.text_input("Image Name:Tag")
    if st.button("Build Image"):
        try:
            msg = build_image(dockerfile_path, image_name)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

elif menu == "List Local Docker Images" or menu == "📦 List Local Docker Images":
    st.header("Local Docker Images")
    if st.button("List Images"):
        try:
            output = list_images()
            st.text(output)
        except Exception as e:
            st.error(str(e))

elif menu == "Search Local Docker Image" or menu == "🔍 Search Local Docker Image":
    st.header("Search Local Docker Images")
    query = st.text_input("Image name or tag to search")
    if st.button("Search Local Images"):
        try:
            output = search_local_images(query)
            st.text(output)
        except Exception as e:
            st.error(str(e))

elif menu == "Search Image on DockerHub" or menu == "🌐 Search Image on DockerHub":
    st.header("Search DockerHub Images")
    query = st.text_input("Image name to search on DockerHub")
    if st.button("Search DockerHub"):
        try:
            output = search_dockerhub(query)
            st.text(output)
        except Exception as e:
            st.error(str(e))

elif menu == "Pull Docker Image" or menu == "⬇️ Pull Docker Image":
    st.header("Pull Docker Image")
    image_name = st.text_input("Image name to pull")
    if st.button("Pull Image"):
        try:
            msg = pull_image(image_name)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

# -------------------- Docker Containers --------------------
elif menu == "List Running Containers" or menu == "📋 List Running Containers":
    st.header("Running Containers")
    if st.button("List Containers"):
        try:
            output = list_running_containers()
            st.text(output)
        except Exception as e:
            st.error(str(e))

elif menu == "Stop Container" or menu == "⏹️ Stop Container":
    st.header("Stop Docker Container")
    container_id = st.text_input("Container ID or name to stop")
    if st.button("Stop Container"):
        try:
            msg = stop_container(container_id)
            st.success(msg)
        except Exception as e:
            st.error(str(e))
