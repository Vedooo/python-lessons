# lambda arguments: expression

# add10 = lambda x: x + 10
# print(add10(5))

# it's same with normal fuction

# def add10_func(x):
#     return print(x + 10)

# add10_func(5)

# mult = lambda x,y: x * y
# print(mult(10,20))

# -----

# points = [(3,9),(3,4),(5,10),(2,7),(6,2)]
# points_sorted = sorted(points)

# points_sorted1 = sorted(points, key=lambda x: x[1])
# # it's same with normal fuction
# def sort_by_y(x):
#     return x[1]

# points_sorted_w_func = sorted(points, key=sort_by_y)

# print(points)
# print(points_sorted)
# print(points_sorted1)
# print(points_sorted_w_func)

# ------
# map(func, seq)

# a = [1,2,3,4,5]

# b = map(lambda x: x * 2, a)
# print(list(b))

# c = [x*2 for x in a]
# print(c)

# ------
# filter(func, seq)

# a = [1,2,3,4,5,6]
# b = filter(lambda x: x%2==0, a)

# print(list(b))

# c = [x for x in a if x%2==0]
# print(c)

# ------
# reduce(func, seq)
# from functools import reduce

# a = [1,2,3,4,5,6,7,8,9,10]

# product_a = reduce(lambda x,y: x * y, a)
# print(product_a)