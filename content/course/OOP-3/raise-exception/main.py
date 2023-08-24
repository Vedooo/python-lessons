# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError: # If except block catch the error it will always work first
#     file = open("a_file.txt", mode='w')
#     file.write("Some")
# except KeyError as error_message:
#     print(f"Key {error_message} doesn't exist")
# else: # What else do you wanna do ?
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is a message I made up")


height = float(input("height: "))
weight = int(input("weight: "))

if height > 2.10:
    raise ValueError("Unreal height value")

bmi = weight / height ** 2

print(bmi)