
#Immutable Example

x = 5  # Create integer object with value 5
y = x  # y now references the same object as x

print(id(x))  # Print memory address of x
print(id(y))  # Same as x

# This creates a NEW integer object with value 6
x=x+1

print(id(x))  # Different address now
print(id(y))  # Still points to original object
print(y)      # Still 5
print(x)      # gives 6

# ..................................................................................

#Mutable Example

numbers=[1,2,3]
numbers_copy=numbers   # Both variables reference the same list

print(id(numbers))
print(id(numbers_copy))  # Same as numbers

numbers.append(4)  # Modifies the existing list

print(numbers)        # [1, 2, 3, 4]
print(numbers_copy)   # [1, 2, 3, 4] - also changed!
print(id(numbers) == id(numbers_copy))  # True - same object