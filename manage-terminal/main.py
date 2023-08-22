import os
from docker_class import Dockerm

docker = Dockerm()

bot_on = True
while bot_on:
    user_request = input("Docker process(info, create, delete_container, delete_image): ")
    
    if user_request == "info":
        docker.container_info()
    elif user_request == "create":
        docker.create()
    elif user_request == "delete_container":
        docker.delete_container()
    elif user_request == "delete_image":
        docker.delete_image()
    elif user_request == "exit":
        bot_on = False
