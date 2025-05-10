#1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

user_input = int(input("Enter a number : "))
def square(n):
    return n**2
result= square(user_input)
print("Square of number is " ,result)