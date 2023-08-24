def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")
            
prime_checker(1902)