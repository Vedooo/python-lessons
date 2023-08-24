numbers = []
for i in range(1,101):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)       
print("Total of all even numbers between 1 to 100 is {}".format(sum(numbers)))