#4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area = round(math.pi * radius ** 2)
    circumference = round(2 * math.pi * radius)
    return area, circumference

area, circumference = circle(4)
print("Area is:", area)
print("Circumference is:", circumference)

