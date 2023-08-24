# age: int
# name: str
# height: float
# is_human: bool

def police_check(age: int) -> bool: # means Function has to return bool
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "They can drive"

if police_check(20):
    print("pass")
else:
    print("pay a fine")