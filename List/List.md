
# Python Lists - Complete Guide

Lists are one of the most versatile and commonly used data structures in Python. They store ordered collections of items that can be of any data type.
List are mutable.

## Creating Lists

```python
# Creating a list of strings
users = ["ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary"]

# Creating an empty list
empty_list = []
```

## Accessing List Elements

```python
users = ["ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary"]

# Using positive index (starts from 0)
print(users[0])  # Output: ElonMusk
print(users[2])  # Output: Harkirat Singh

# Using negative index (starts from -1)
print(users[-1])  # Output: Hitesh Choudhary
print(users[-2])  # Output: Harkirat Singh
```

## List Slicing

Slicing allows you to extract a portion of the list using the syntax `list[start:stop]`.

```python
users = ["ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary"]

# Get elements from index 1 to 2 (not including 3)
print(users[1:3])  # Output: ['Sam Altman', 'Harkirat Singh']

# Get all elements from index 2 to the end
print(users[2:])  # Output: ['Harkirat Singh', 'Hitesh Choudhary']

# Get all elements from beginning to index 2 (not including 2)
print(users[:2])  # Output: ['ElonMusk', 'Sam Altman']
```

## Modifying Lists

### Replacing Elements Using Slicing

```python
users = ["ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary"]

# Important: When replacing with slicing, you must provide an iterable -> they are treated like an array while replacing using slicing
# This replaces a single element with multiple characters
users[1:2] = "Piyush Garg"  # String is treated as an iterable of characters
print(users)  # Output: ['ElonMusk', 'P', 'i', 'y', 'u', 's', 'h', ' ', 'G', 'a', 'r', 'g', 'Harkirat Singh', 'Hitesh Choudhary']

# To replace with the complete name, use a list with one element
users = ["ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary"]
users[1:2] = ["Piyush Garg"]
print(users)  # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']
```

### Inserting Elements with Slicing

```python
users = ["ElonMusk", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]

# Insert at position 1 without replacing elements
users[1:1] = ["Sam Altman"]  
print(users)  # Output: ['ElonMusk', 'Sam Altman', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']
```

### Removing Elements with Slicing

```python
users = ["ElonMusk", "Sam Altman", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]

# Remove element at index 1
users[1:2] = []  
print(users)  # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']
```

## List Operations

### Iterating Through a List

```python
users = ["ElonMusk", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]

# Print each name on a new line
for name in users:
    print(name)

# Print each name with a separator
for name in users:
    print(name, end="-")
# Output: ElonMusk-Piyush Garg-Harkirat Singh-Hitesh Choudhary-
```

### Checking if an Element Exists

```python
users = ["ElonMusk", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]

if "Hitesh Choudhary" in users:
    print("Name exists")  # Output: Name exists
```

### Adding Elements

```python
users = ["ElonMusk", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]

# Add to the end of the list
users.append("Sam Altman")
print(users)  # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary', 'Sam Altman']

# Insert at a specific position
users = ["Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]
users.insert(0, "ElonMusk")
print(users)  # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']
```

### Removing Elements

```python
users = ["ElonMusk", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary", "Sam Altman"]

# Remove and return the last element
last_user = users.pop()
print(last_user)  # Output: Sam Altman
print(users)  # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']

# Remove by value
users.remove("ElonMusk")
print(users)  # Output: ['Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']
```

## Working with Copies vs. References

```python
users = ["ElonMusk", "Piyush Garg", "Harkirat Singh", "Hitesh Choudhary"]

# Creating a reference (changes to one affect the other)
users_ref = users #Refernce in the memory will go to user_ref , but we dont need same refercne we need new copy so in pyhton we can use copy() - different references

# Creating a new copy (changes to one don't affect the other)
users_copy = users.copy()
users_copy.append("Sam Altman")

print(users_copy)  # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary', 'Sam Altman']
print(users)      # Output: ['ElonMusk', 'Piyush Garg', 'Harkirat Singh', 'Hitesh Choudhary']
```

## List Comprehension

List comprehension provides a concise way to create lists based on existing lists or iterables.

```python
# Create a list of squared numbers from 0 to 9
squared_num = [x**2 for x in range(10)]
print(squared_num)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension with conditional
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
```

## The `range()` Function

The `range()` function generates a sequence of numbers, commonly used in loops.

```python
# range(stop) - generates numbers from 0 to stop-1
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# range(start, stop) - generates numbers from start to stop-1
for i in range(2, 5):
    print(i)  # Output: 2, 3, 4

# range(start, stop, step) - generates numbers from start to stop-1 with step
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8
```

## Common List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# Sort the list in-place
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Reverse the list in-place
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Count occurrences of an element
count = numbers.count(1)
print(count)  # Output: 2

# Find index of first occurrence
index = numbers.index(5)
print(index)  # Output: 1

# Extend list with another list
numbers.extend([6, 5, 3])
print(numbers)  # Output: [9, 5, 4, 3, 2, 1, 1, 6, 5, 3]

# Clear all elements
numbers.clear()
print(numbers)  # Output: []
```