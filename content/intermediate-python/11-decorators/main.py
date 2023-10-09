## Syntax
# @mydecorator
# def dosmonething():
#     pass

import functools # 2) For fixing usage using functools

## Decorator template
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         # Do...
#         result = func(*args,**kwargs)
#         # Do...
#         return result
#     return wrapper

# def start_end_decorator(func):
    
#     @functools.wraps(func) # 2) For fixing usage using functools decorator
#     def wrapper(*args,**kwargs):
#         print('start')
#         func(*args,**kwargs)
#         print('end')
#         return result # 1) For fixing functions result adding return "value"
#     return wrapper

##  Using decorator is same thing with call functions
# @start_end_decorator
# def print_name():
#     print('Alex')

# print_name = start_end_decorator(print_name)

# @start_end_decorator
# def add(x):
#     return x * 5

# result = add(5) # 1)This will print none
# print(help(add))
# print(add.__name__) # 2) This will return none 


# -----

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
        
# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}')
    
# greet('Alex') # It will print 4 times the name

# -----

## Multiple Decorators

# def start_end_decorator(func):
    
#     @functools.wraps(func) # 2) For fixing usage using functools decorator
#     def wrapper(*args,**kwargs):
#         print('start')
#         result = func(*args,**kwargs)
#         print('end')
#         return result # 1) For fixing functions result adding return "value"
#     return wrapper

# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting

# say_hello('Alex')

# -----

## Class Decorator

# class CountCalls():
    
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0
        
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f'This is executed {self.num_calls} times')
#         return self.func(*args, **kwargs)
#         # print('Hi there')
        
# cc = CountCalls(None) # Calls hi there 
# cc()


# @CountCalls
# def say_hello():
#     print('Hello')

# say_hello()
# say_hello()
# say_hello()
# say_hello()







