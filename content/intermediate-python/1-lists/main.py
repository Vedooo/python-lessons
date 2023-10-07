## Function of lists

# mylist = ["banana", "apple", "orange"]

# if "apple" in mylist:
#     print("yes")
# else:
#     print("no")
    
    
# mylist.append("lemon")
# print(f"append: {mylist}")

# mylist.insert(1,"blueberry")
# print(f"insert: {mylist}")

# item = mylist.pop()
# print(item)
# print(f"append: {mylist}")

# mylist.remove("orange")
# print(f"remove: {mylist}")

# mylist.sort()
# print(f"sort: {mylist}")

# newlist = sorted(mylist)
# print(f"sorted newlist: {newlist}")


# mylist.reverse()
# print(f"reverse: {mylist}")


## Ordered, mutable, allows dublicate elements

# mylist = [0] * 5
# print(mylist)
# mylist2 = [1,2,3,4,5]

# newlist = mylist + mylist2
# print(newlist)

# -----
# mylist = [1,2,3,4,5,6,7,8,9]

# a = mylist[1:5] # --> Distance 
# print(a)

# a = mylist[:5] # --> last index
# print(a)

# a = mylist[::2] # --> step 
# print(a)

# -----
# list_org = ["banana", "cherry", "apple"]

# list_cpy = list_org
# list_cpy = list_org.copy()
# list_cpy = list(list_org)
# list_cpy = list_org[:]

# list_cpy.append("lemon")

# print(list_org)
# print(list_cpy)

# -----

# mylist = [1,2,3,4,5,6]
# b = [i*i for i in mylist]

# print(mylist)
# print(b)