# Errors and Exceptions

## TypeError: unsupported operand type(s) for +: 'int' and 'str'

# a = 5 + '10'

## ImportError: ModuleNotFoundError: No module named 'somemodule'

# import somemodule

## NameError: name 'c' is not defined

# a = 5
# b = c

## FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

# f = open('somefile.txt')

## ValueError: list.remove(x): x not in list

# a = [1,2,3]
# a.remove(4)
# print(a)

## IndexError: list index out of range

# a = [1,2,3]
# a[4]
# print(a)

## KeyError: 'age'

# mydict = {'name': 'max'}
# mydict['age']


## Raise error

# x = -5

# if x < 0:
#     raise Exception('x should be positive')

## Assert: AssertionError

# x = -5
# assert (x >= 0), 'x is not possitive'

## Try-except blocks

# try:
#     a = 5 / 0 
# except:
#     print('an error happend')

# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)

# try:
#     a = 5 / 0
#     b = a + '10'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
    
# try:
#     a = 5 / 1
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("it's okey")
      
# try:
#     a = 5 / 0
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("it's okey")
# finally:
#     print("cleaning up...")


## Create own error class

# class ValueTooHighError(Exception):
#     pass

# class ValueTooSmallError(Exception):
#     def __init__(self, message, value): 
#         self.message = message
#         self.value = value

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('value is too high')
#     if x < 5:
#         raise ValueTooSmallError('value is too small', x)

# try:
#     test_value(1)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmallError as e:
#     print(e.message, e.value)