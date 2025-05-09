#2. Sum of Even Numbers
#Problem: Calculate the sum of even numbers up to a given number n.

number = int(input('Enter n number: '))
sum_of_number = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum_of_number += num

print("Sum of even numbers up to", number, "is :", sum_of_number)
