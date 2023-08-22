from art import logo

print(logo)

customer_list = {}
while True:
    name_of_customer = input("Your name: ").lower()
    if name_of_customer.lower() == 'no':
        break
    
    bid_of_customer = int(input("Your bid? "))
    customer_list[name_of_customer] = bid_of_customer   
print(customer_list)
winner = max(customer_list, key=customer_list.get)

print(f"Winner is {winner}")