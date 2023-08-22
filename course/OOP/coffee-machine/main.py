from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# from replit import clear

machine_on = True
menu = Menu()
machine = MoneyMachine()
maker = CoffeeMaker()

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        maker.report()
        machine.report()
    if choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
          maker.make_coffee(drink)         
    