import json
from typing import Any

person = {
    "firstname": "Jane",
    "lastname": "Doe",
    "hobbies": [
        "running", "swimming", "singing",
    ],
    "age": 27,
    "hasChildren": True,
    "children": [
        {
            "firstname": "Alex",
            "age": 5
        },
        {
            "firstname": "Bob",
            "age":7
        }
    ]
}

## Can create manually with data 

# personJson = json.dumps(person, 
#                         indent=4) 
#                         # separators=('; ', '= ')
#                         # sort_keys=True
# print(personJson)

## or create as file with file open method

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# -----

# personJson = json.dumps(person, indent=4)
# person = json.loads(personJson)
# print(person)

# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

# -----

# class User:
#     def __init__(self, name, age):
#         self.name: str = name
#         self.age: int = age
        
# user = User(name="Max", age=26)

## First way: Create encoder function for "TypeError: Object of type User is not JSON serializable"
# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError('Object of type User is not JSON serializable')

## Second way: implement custom Json Encoder for serializing
# from json import JSONEncoder
# class UserEnconder(JSONEncoder):
#     def default(self, o: Any):
#         if isinstance(o, User):
#             return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#         return JSONEncoder.default(self, o)

## First way usage
# userJson = json.dumps(user, default=encode_user, indent=4)
# print(userJson)

# Second way usage
# userJson = UserEnconder().encode(user)
# print(userJson)

## For decode json dict
# def decode_user(dct):
#     if User.__name__ in dict:
#         return User(name=dct['name'], age=dct['age'])
#     return dct 

# user = json.loads(userJson, object_hook=decode_user)
# print(type(user))
# print(user.name)


