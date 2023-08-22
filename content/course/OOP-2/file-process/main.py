file = open("main.txt")
print(file.read())


with open("new_file.txt", mode="w") as file:
    file.write("\nVedo is woring.")