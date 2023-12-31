# TODO: Print report
# TODO: Check resources sufficent ?
# TODO: Process coins
# TODO: Check transaction succesfully?
# TODO: Make coffee



"""
1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
    a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
    dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “​off”​to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    the machine. Your code should end execution when this happens.
3. Print report.
    a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
        
4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “​Sorry there is not enough water.”​
    c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “​Sorry that's not enough money. Money refunded.​”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    c. If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

7. Make Coffee.
    a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
    E.g. report before purchasing latte: Water: 300ml
    Milk: 200ml
    Coffee: 100g
    Money: $0
    Report after purchasing latte:
            Water: 100ml
            Milk: 50ml
            Coffee: 76g
            Money: $2.5
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

"""
from menu import resources
from menu import menu
from money import coins
from replit import clear

def report():
    water  = resources["water"]
    milk   = resources["milk"]
    coffee = resources["coffee"]
    return print(f"Current resource amounts are:\n {water}\n {milk}\n {coffee}\n")

def check_amount(money, choice):    
    if choice in menu:
        if money >= menu[choice]["cost"]:
            print(f"Here is your {choice}")
            money -= menu[choice]["cost"]
        else:
            print(f"{money} is not enough for {choice}")
    else:
        print("Invalid choice")
    return money

def process_coins(qty_quarters, qty_dimes, qty_nickles, qty_penniess):
    return qty_quarters * coins["quarters"] + qty_dimes * coins["dimes"] + qty_nickles * coins["nickles"] + qty_penniess * coins["pennies"]

def make_coffee(choice, resources):
    if choice in menu:
        drink = menu[choice]
        ingredients = drink["ingredients"]
        
        for ingredient, amount in ingredients.items():
            if resources[ingredient] >= amount:
                resources[ingredient] -= amount
            else:
                print(f"Sorry, not enough {ingredient}.")
                return False  # Kaynaklar yetersizse False döndürüyoruz
        return True  # Başarıyla içecek yapılabilirse True döndürüyoruz
    else:
        print("Invalid choice.")
        return False

machine_on = True
process = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice != "report" and choice != "off":
        while process:
            qty_quarters = int(input(f"Please insert quarters: "))
            qty_dimes = int(input(f"Please insert dimes: "))
            qty_nickles = int(input(f"Please insert nickles: "))
            qty_penniess = int(input(f"Please insert penniess: "))
            money = process_coins(qty_quarters, qty_dimes, qty_nickles, qty_penniess)
            if make_coffee(choice, resources):
                money = check_amount(money, choice)
            else:
                print("Coffee couldn't be made.\n")
                machine_on = False
            print(f"Here is your change {money}\n Thank you")
            break
    if choice == "report":
        clear()
        report()
        continue
    if choice == "off":
        clear()
        machine_on = False