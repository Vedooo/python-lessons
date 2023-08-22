from art import logo
import os

print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operator = {
    "+": add,
    "-": subtract,
    "*": multi,
    "/": divide
}

restart = True
while restart:
    num1 = int(input("What is your first number? "))
    num2 = int(input("What is your second number? "))

    for symbol in operator:
        print(symbol)

    operator_symbol = input("Pick a operation symbol..")
    if operator_symbol not in operator:
        raise TypeError("Please pick a valid operations")

    calculation_function = operator[operator_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    
    again = input("Press y for restart or n for quit: ")
    if again == "y":
        restart == True
        os.system("clear")
    elif again == "n":
        print("Goodbye")
        break
        
        