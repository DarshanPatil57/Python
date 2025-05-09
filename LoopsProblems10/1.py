#1. Counting Positive Numbers
#Problem: Given a list of numbers, count how many are positive.


numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count=0
for n in numbers:
    if n > 0:
        count +=1
print("Positive numbers are :",count)
