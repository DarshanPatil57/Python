#7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_of_all(*args):
#    print(args)
#    print(*args)
    for i in args:
        print(i*2)
    return sum(args)

# print(sum_of_all(1,2,3,4,5))
print("Sum : " ,sum_of_all(1,2))