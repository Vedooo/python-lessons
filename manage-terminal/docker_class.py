import os
import subprocess as sp
import time as t

SYSTEM_MESSAGES = ["Your container is creating..", "Getting container informations", "Container deleting.."]


class Dockerm:
    def __init__(self) -> None:
        pass
     
    def create(self):
        container_name = input("Set container name: ")
        container_name_arg = f"--name {container_name}"
        
        image_name = input("Set image: ")
        
        port_input = input("Set port (or type 'no'): ")
        port_arg = f"-p {port_input}" if port_input != "no" else ""
        
        volume_input = input("Set volume (or type 'no'): ")
        volume_arg = f"--volume {volume_input}" if volume_input !="no" else ""
        
        network_input = input("Set network (or type 'no'): ")
        network_arg = f"--network {network_input}" if network_input !="no" else ""
        
        connect_interactive = input("Connect interactive (yes or type 'no'):")
        connect_arg = "-it" if connect_interactive !="no" else ""
        
        os.system(f"docker container run {container_name_arg} {connect_arg} {port_arg} {volume_arg} {network_arg} {image_name}")
       
    def container_info(self):
        os.system("docker container ls -a")
        
    def delete_container(self):
        container_id = input("Container id to delete: ")
        os.system(f"docker container rm -f {container_id}")
        
    def delete_image(self):
        image_id = input("Image id to delete: ")
        os.system(f"docker container rm -f {image_id}")