import string
import random as rd

alphabet = list(string.ascii_lowercase)
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['+','%','&','/','#','?','*','-']

nr_alphabet = int(input("How many letter you want in password? "))
nr_numbers = int(input("How many number you want in password? "))
nr_symbols = int(input("How many symbol you want in password? "))

password_list = []

for i in range (1, nr_alphabet + 1):
    password_list += rd.choice(alphabet)

for i in range (1, nr_numbers + 1):
    password_list += rd.choice(numbers)
    
for i in range (1, nr_symbols + 1):
    password_list += rd.choice(symbols)

rd.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)

