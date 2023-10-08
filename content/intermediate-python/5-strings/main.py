# Strings: ordered, immutable, text representation

# mysting = 'I\'am a programmer'
# mysting2 = "I'am a programmer"
# mysting3 = """Hello\
#  world"""

# mystring4 = "Hello world"
# char = mystring4[-1]
# substring = mystring4[1:5]
# substring1 = mystring4[:5]
# substring2 = mystring4[:]
# substring3 = mystring4[::2]
# substring4 = mystring4[::-1]


# print(mysting)
# print(mysting2)
# print(mysting3)
# print(char)
# print(substring)
# print(substring1)
# print(substring2)
# print(substring3)
# print(substring4)

# -----

# greeting = "Hello"
# name = "Tom"
# sentence = greeting + " " + name
# print(sentence)

# -----

# greeting = "Hello"
# for i in greeting:
#     print(i)
    
# if "ell" in greeting:
#     print("yes")
# else:
#     print("no")

# -----

# mystring = '     hello world     '
# mystring = mystring.strip() # Strip space, \* types chars 

# mystring = "Hello world"
# print(mystring.lower())
# print(mystring.upper())
# print(mystring.startswith('Hello'))
# print(mystring.endswith('World'))
# print(mystring.find('o'))
# print(mystring.count('l'))
# print(mystring.replace('world', 'universe'))

# print(mystring)v

# -----

# mystring = 'how are you doing'
# mystring1 = 'how,are,you,doing'

# mylist = mystring.split() # ['how', 'are', 'you', 'doing']
# mylist1 = mystring1.split(",") # ['how are you doing']

# new_string = ''.join(mylist1) # howareyoudoing
# new_string1 = ' '.join(mylist1) # how are you doing

# print(mylist)
# print(mylist1)
# print(new_string)
# print(new_string1)

# -----

# from timeit import default_timer as timer

# mylist = ['a'] * 1000000
# #print(mylist)

# # bad
# start = timer()
# mystring = ''
# for i in mylist:
#     mystring += i
# stop = timer()
# print(stop - start)

# # good
# start = timer()
# mystring = ''.join(mylist) # ****
# stop = timer()
# print(stop - start)