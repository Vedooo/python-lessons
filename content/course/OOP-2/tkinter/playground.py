# def add(*args):
#     return print(sum(args))


# def calculate(**kwargs):
#     for key, value in kwargs.items():
#         return print(f"{key}: {value}")
        
        
# calculate(add=3, multiple=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        
        
my_car = Car(make="falan", model="530")
print(my_car)