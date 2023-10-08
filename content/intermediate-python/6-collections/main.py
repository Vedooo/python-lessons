
# Collections: Counter, namedtuple, ordereddict, defaultdict, deque

# from collections import Counter

# a = "aaaabbbbbcccc"

# mycounter = Counter(a)
# print(mycounter) # Counter({'a': 4, 'b': 4, 'c': 4})
# print(mycounter.keys())
# print(mycounter.values())
# print(mycounter.items())
# print(mycounter.most_common())
# print(mycounter.most_common(3)[0]) # access the element
# print(mycounter.most_common(3)[0][0]) # access the elements index
# print(list(mycounter.elements()))

# ------

# from collections import namedtuple

# Point = namedtuple('Point', 'x,y') # Create a class called point and args

# pt = Point(1, -4)
# print(pt.x, pt.y)

# ------

# from collections import OrderedDict

# ordered_dict = OrderedDict()
# ordered_dict["a"] = 1
# ordered_dict["b"] = 2
# ordered_dict["c"] = 3
# ordered_dict["d"] = 4

# print(ordered_dict)

# ------

# from collections import defaultdict

# d = defaultdict(int) # allow the all types: lists, strings, floats, ...
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3

# ------

# from collections import deque

# d = deque()

# d.append(1)
# d.append(2)
# d.appendleft(3)

# d.pop()
# d.popleft()

# d.clear()

# d.extend([1,2,3])
# d.extendleft([4,5,6])

# d.rotate(1)
# d.rotate(-11)

# print(d)