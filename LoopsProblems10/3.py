#3. Multiplication Table Printer
#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input('Enter a number: '))

for num in range(1,11):
    if num == 5:
        continue
    print(number , 'x' , num ,'=' , number*num)