#9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.



# 🧠 Imagine This:
# Think of a generator like a magic vending machine.

# Normally, when you call a function, it runs, does its work, and gives you everything at once.

# But a generator function (using yield) is like a vending machine that gives you one item at a time, every time you ask.

# 🔄 yield vs return

# return:

# Gives back a final answer and ends the function
# Function ends after return
# Good for one result

#	yield:

# Gives one result, then pauses and remembers where it stopped
# Function keeps going from where it left off next time
# Good for a sequence of results

# Example: Your Code

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
# Let’s say limit = 10. The generator will go like this:

# Starts at 2

# Sees yield 2 → gives 2 (pauses here)

# Next time you ask → gives 4

# Then 6, then 8, then 10

# Then it’s done!

for num in even_generator(10):
    print(num)
# This tells Python: "Keep asking the vending machine for the next even number until it stops."

def even_generator(limit):
    for i in range(2,limit + 1 , 2):
        yield i

for num in even_generator(10):
    print(num)
