# Sets: unordered, mutable, no duplicates

#myset = {1,2,3}
# myset_emt = set()
# myset1 = set([1,2,3])
# myset2 = set("hello")
# myset_no_dublicate = {1,2,3,1,2,3}

# print(myset)
# print(myset1)
# print(myset2)
# print(myset_no_dublicate)
# print(type(myset))

# -----

# myset = set() 

# myset.add(1)
# myset.add(2)
# myset.add(3)

# myset.discard(3)
# myset.pop()
# myset.clear()

# for x in myset:
#     print(x)

# if 1 in myset:
#     print("yes")
# if 4 in myset:
#     print("also yes")
# else:
#     print("no")

# print(myset)

# -----

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# union = odds.union(evens)
# intersection = odds.intersection(evens)
# intersection_w_prime = odds.intersection(primes)
# intersection_even_w_prime = evens.intersection(primes)


# print(union)
# print(intersection)
# print(intersection_w_prime)
# print(intersection_even_w_prime)

# -----

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}

# diff = setA.difference(setB)
# diff_sym = setB.symmetric_difference(setA) # ---> these are create new set

# print(diff)
# print(diff_sym)

# setA.update(setB)
# setA.intersection_update(setB) 
# setA.difference_update(setB)  
# setA.symmetric_difference_update(setB) # ---> these are update current set

# print(setA)

# -----

# setA = {1,2,3,4,5,6}
# setB = {1,2,3}

# print(setA.issubset(setB)) # False
# print(setB.issubset(setA)) # True

# print(setB.issuperset(setA)) # False
# print(setA.issuperset(setB)) # True

# print(setB.isdisjoint(setA)) # False
# print(setA.isdisjoint(setB)) # True

# -----

# setA = {1,2,3,4,5,6}
# setB = setA

# setB.add(7)

# print(setB)
# print(setA)

# -----

# a = frozenset([1,2,3,4]) # cannot change the content of frozensets!

# a.add(5) # Attribute error
# a.remove(5) # Attribute error

# print(a)