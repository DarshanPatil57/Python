#8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("Enter a number : "))
is_prime =True
if number > 1:
        for i in range(2,number):
                if (number % 2 == 0):
                        is_prime = False
                        break
print("Number is prime : ", is_prime)