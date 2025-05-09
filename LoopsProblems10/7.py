#7. Validate Input
#Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a number : "))
    if 1<= number <= 10:
        print("Input between 1 and 10 range. New level unloked")
        break
    else:
        print("Invalid input")



