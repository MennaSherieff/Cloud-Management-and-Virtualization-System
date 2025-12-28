import streamlit as st
import subprocess

# --- IMPORT BACKEND FUNCTIONS (NO CHANGES) ---
from vm.vm_manager import interactive_mode, config_mode
from docker.dockerfile_manager import create_dockerfile
from docker.image_manager import (
    build_image, list_images, search_local_images, 
    search_dockerhub, pull_image
)

#CONTAINER FUNCTIONS
def list_running_containers():
    result = subprocess.check_output(["docker", "ps"], text=True)
    return result

def list_all_containers():
    result = subprocess.check_output(["docker", "ps", "-a"], text=True)
    return result

def stop_container(container_id):
    subprocess.run(["docker", "stop", container_id], check=True)
    return f"Container {container_id} stopped."

def delete_container(container_id):
    subprocess.run(["docker", "rm", container_id], check=True)
    return f"Container {container_id} deleted."


#PAGE CONFIG
st.set_page_config(page_title="Cloud Management System", layout="wide")
st.title("☁️ Cloud Management & Virtualization Dashboard")

# Sidebar menu
menu = st.sidebar.radio("⚙ Select Feature", [
    "🖥 Create VM (Interactive)",
    "📁 Create VM from Config File",
    "📄 Create Dockerfile",
    "🏗 Build Docker Image",
    "📦 List Local Docker Images",
    "🔍 Search Local Docker Image",
    "🌐 Search DockerHub Images",
    "⬇ Pull Docker Image",
    "🚀 List Running Containers",
    "📋 List All Containers",
    "⛔ Stop Container",
    "🗑 Delete Container"
])

#VM SECTION
if menu == "🖥 Create VM (Interactive)":
    st.subheader("Interactive QEMU VM Creation")

    col1, col2, col3 = st.columns(3)
    with col1:
        cpu = st.number_input("CPU Cores", 1, 16, 2)
    with col2:
        memory = st.number_input("Memory (MB)", 256, 32768, 2048)
    with col3:
        disk_size = st.text_input("Disk Size", "10G")

    if st.button("Launch VM"):
        try:
            interactive_mode(cpu, memory, disk_size)
            st.success("VM started successfully!")
        except Exception as e:
            st.error(str(e))


elif menu == "📁 Create VM from Config File":
    st.subheader("Create VM using config.txt")
    if st.button("Run Config Mode"):
        try:
            config_mode()
            st.success("VM created from config.txt successfully!")
        except Exception as e:
            st.error(str(e))

#DOCKERFILE
elif menu == "📄 Create Dockerfile":
    st.subheader("Dockerfile Generator")

    path = st.text_input("Save Directory")
    content = st.text_area("Dockerfile Content")

    if st.button("Generate"):
        try:
            lines = content.strip().split("\n")
            msg = create_dockerfile(path, lines)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

#IMAGE BUILD
elif menu == "🏗 Build Docker Image":
    st.subheader("Image Builder")

    c1, c2 = st.columns(2)
    with c1:
        dockerfile_path = st.text_input("Dockerfile Path")
    with c2:
        image_name = st.text_input("Image Name:Tag")

    if st.button("Build"):
        try:
            msg = build_image(dockerfile_path, image_name)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

#LIST IMAGES
elif menu == "📦 List Local Docker Images":
    st.subheader("Local Docker Images")
    if st.button("Show Images"):
        try:
            output = list_images()
            st.code(output, language="bash")
        except Exception as e:
            st.error(str(e))

#SEARCH LOCAL IMAGES
elif menu == "🔍 Search Local Docker Image":
    st.subheader("Search Local Docker Images")
    query = st.text_input("Search Name")
    if st.button("Search"):
        try:
            output = search_local_images(query)
            st.code(output, language="bash")
        except Exception as e:
            st.error(str(e))

#SEARCH DOCKERHUB
elif menu == "🌐 Search DockerHub Images":
    st.subheader("DockerHub Search")
    query = st.text_input("DockerHub Image Name")
    if st.button("Search"):
        try:
            output = search_dockerhub(query)
            st.code(output, language="bash")
        except Exception as e:
            st.error(str(e))

#PULL IMAGE
elif menu == "⬇ Pull Docker Image":
    st.subheader("Pull DockerHub Image")
    image_name = st.text_input("Image to Pull")
    if st.button("Pull"):
        try:
            msg = pull_image(image_name)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

#CONTAINER LIST
elif menu == "🚀 List Running Containers":
    st.subheader("Running Containers")
    if st.button("Run"):
        try:
            output = list_running_containers()
            st.code(output, language="bash")
        except Exception as e:
            st.error(str(e))

elif menu == "📋 List All Containers":
    st.subheader("All Containers")
    if st.button("List"):
        try:
            output = list_all_containers()
            st.code(output, language="bash")
        except Exception as e:
            st.error(str(e))

#STOP CONTAINER
elif menu == "⛔ Stop Container":
    st.subheader("Stop Docker Container")
    cid = st.text_input("Container ID / Name")
    if st.button("Stop"):
        try:
            msg = stop_container(cid)
            st.success(msg)
        except Exception as e:
            st.error(str(e))

#DELETE CONTAINER
elif menu == "🗑 Delete Container":
    st.subheader("Remove Docker Container")
    cid = st.text_input("Container ID / Name")
    if st.button("Delete"):
        try:
            msg = delete_container(cid)
            st.success(msg)
        except Exception as e:
            st.error(str(e))


