# Dictionaries: Key-Value pairs, Unordered, Mutable

# mydict = {"name": "Kayle", "age": 27, "city": "Boston"}
# print(mydict)

# mydict2 = dict(name="Mary", age=27, city="Boston")
# print(mydict2)

# value = mydict["name"]
# value2 = mydict["lastname"]
# print(value)
# print(value2) # Key value error

# -----

# mydict = {"name": "Kayle", "age": 27, "city": "Boston"}
# print(mydict)

# mydict["email"] = "kayle@gmail.com" # add new key
# print(mydict)

# mydict["email"] = "falan@gmail.com" # change the key
# print(mydict)

# del mydict["name"] # delete the key
# print(mydict)

# mydict.pop("age") # delete the key
# print(mydict)

# mydict.popitem() # delete last key
# print(mydict)

# try:
#     print(mydict["name"])
# except:
#     print("Error")
    
# try:
#     print(mydict["lastname"])
# except:
#     print("Error")
# finally:
#     mydict["lastname"] = "koc"
#     print(mydict)    

# -----

# for key in mydict:
#     print(key)
    
# for key in mydict.keys():
#     print(key)
    
# for value in mydict:
#     print(value)
    
# for value in mydict.values():
#     print(value)
    
# for key, value in mydict.items():
#     print(f"{key}: {value}")

# -----

# mydict_cpy = mydict
# mydict_cpy1 = dict(mydict)
# mydict_cpy2 = mydict.copy()

# print(mydict_cpy)

# mydict_cpy["email"] = "falan@gmail.com"
# print(mydict)

# mydict2 = dict(name="Mary", age=26, email="falan@gmail.com")
# print(mydict2)

# mydict.update(mydict2)
# print(mydict)

# -----
# mydict = {3: 9, 4: 16, 5: 25}
# print(mydict)

# # value = mydict[0]
# # print(value) # --> gives KeyError: 0

# # value2 = mydict[3]
# # print(value2)

# mytuple = (8, 7)
# mydict = {mytuple: 15}

# print(mydict)