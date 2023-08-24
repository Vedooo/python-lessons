# File Error

# with open("a_file.txt") as file:
#     file.read()

# Key Error
# a_dictionary = {key:value}
# value = a_dictionary["non_exists_value"]

#Index Error
# fruits = ["a","b","c"]
# fruit = fruits[3]


#Type Error
# text = "abc"
# print(text + 5) 



# try = something that might cause an exception
# except = Do this if there was an exception
# else = Do this if there were no exceptions
# finally = Do this no metter what happens


# if try was not be successed then except will be execute 
# try:
#     file = open("a_file.txt")
# except:
#     print("There is a error")

# Try process if not succeded then except block will do the process
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt", mode='w')


# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["asdasd"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode='w')
#     file.write("Some")
# except KeyError as error_message:
#     print(f"Key {error_message} doesn't exist")


# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["asdasd"])
# except FileNotFoundError: # If except block catch the error it will always work first
#     file = open("a_file.txt", mode='w')
#     file.write("Some")
# except KeyError as error_message:
#     print(f"Key {error_message} doesn't exist")
# else: # What else do you wanna do ?
#     content = file.read()
#     print(content)


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

try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError: # If except block catch the error it will always work first
    file = open("a_file.txt", mode='w')
    file.write("Some")
except KeyError as error_message:
    print(f"Key {error_message} doesn't exist")
else: # What else do you wanna do ?
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")