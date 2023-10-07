# Tuple: ordered, immutable, allows, dublicate elements

# mytuple = ("Max", 28, "Boston")

# mytuple2 = tuple("Max", 28, "Boston")
# print(mytuple)
# print(type(mytuple))

# print(mytuple2)
# print(type(mytuple2))

# item = mytuple[0]
# print(item)

# item2 = mytuple2[0]
# print(item2)

# ------
# mytuple = tuple(["Max", 28, "Boston"])
# print(mytuple)

# for i in mytuple:
#     print(i)
    
# if "Max" in mytuple:
#     print("yes")
    
# else:
#     print("no")

# ------

# mytuple = ('a','p','p','l','e')

# print(mytuple.count('p'))
# print(mytuple.index('a'))

# mylist = list(mytuple)
# mylist.append('o')
# print(mylist)

# mytuple2 = tuple(mylist)
# print(mytuple2)

# a = (1,2,3,4,5,6,7,8,9,10)

# b = a[2:5]
# print(b)

# b = a[2:]
# print(b)

# b = a[::2]
# print(b)

# b = a[::-1] # Reverse your tuple
# print(b)

# mytuple = "Max", 28, "Boston"
# print(type(mytuple))

# name, age, city = mytuple

# print(name)
# print(age)
# print(city)

# mytuple = (1,2,3,4,5,6,7,8,9,10)

# i1, i2, *i3 = mytuple

# print(i1)
# print(i2)
# print(i3) # --> Also converting a list

# import sys
# import timeit

# mylist = [0, 1, 2, "hello", True] 
# mytuple = (0, 1, 2, "hello", True)

# print(sys.getsizeof(mylist), "bytes") # 120 bytes
# print(sys.getsizeof(mytuple), "bytes") # 80 bytes

# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # 0.03847379994112998
# print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # 0.0064836000092327595




