# Python Tuples - Complete Guide

Tuples are immutable ordered collections in Python. Unlike lists, once created, their elements cannot be changed, added, or removed.

## Creating Tuples

```python
# Creating a tuple with elements
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with a single element (note the comma!)
single_element = ("Python",)  # The comma is necessary
not_a_tuple = ("Python")  # This is a string, not a tuple

# Creating a tuple without parentheses (using comma separation)
another_tuple = "ElonMusk", "Sam Altman", "Harkirat Singh"
```

## Accessing Tuple Elements

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")

# Using positive index (starts from 0)
print(users[0])  # Output: ElonMusk
print(users[2])  # Output: Harkirat Singh

# Using negative index (starts from -1)
print(users[-1])  # Output: Hitesh Choudhary
print(users[-2])  # Output: Harkirat Singh
```

## Tuple Slicing

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")

# Get elements from index 1 to the end
print(users[1:])  # Output: ('Sam Altman', 'Harkirat Singh', 'Hitesh Choudhary')

# Get elements from beginning to index 2 (not including 2)
print(users[:2])  # Output: ('ElonMusk', 'Sam Altman')

# Get elements from index 1 to 3 (not including 3)
print(users[1:3])  # Output: ('Sam Altman', 'Harkirat Singh')
```

## Immutability of Tuples

The key characteristic of tuples is their immutability. Once created, you cannot change them.

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")

# This will raise an error
# users[0] = 'Piyush Garg'  # TypeError: 'tuple' object does not support item assignment

# Also not allowed:
# users.append("New User")  # AttributeError: 'tuple' object has no attribute 'append'
# users.remove("ElonMusk")  # AttributeError: 'tuple' object has no attribute 'remove'
```

## Tuple Operations

### Finding Length

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")
print(len(users))  # Output: 4
```

### Checking if an Element Exists

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")

if "Hitesh Choudhary" in users:
    print("User exists in tuple")  # Output: User exists in tuple
```

### Counting Occurrences

```python
numbers = (1, 2, 3, 4, 1, 2, 1)
print(numbers.count(1))  # Output: 3

users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")
print(users.count("Hitesh Choudhary"))  # Output: 1
```

### Finding Index of an Element

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")
print(users.index("Sam Altman"))  # Output: 1

# Be careful - raises ValueError if element not found
# print(users.index("Not in tuple"))  # ValueError: tuple.index(x): x not in tuple
```

## Iterating Through a Tuple

```python
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")

# Simple iteration
for user in users:
    print(user)

# Enumerated iteration (to get index and value)
for index, user in enumerate(users):
    print(f"{index}: {user}")
```

## Tuple Unpacking

One of the most useful features of tuples is unpacking:

```python
# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(x)  # Output: 10
print(y)  # Output: 20

# Unpacking with multiple values
user_info = ("ElonMusk", 52, "CEO", "Tesla")
name, age, position, company = user_info

# Extended unpacking (Python 3+)
users = ("ElonMusk", "Sam Altman", "Harkirat Singh", "Hitesh Choudhary")
first, second, *others = users
print(first)   # Output: ElonMusk
print(others)  # Output: ['Harkirat Singh', 'Hitesh Choudhary']

first, *middle, last = users
print(middle)  # Output: ['Sam Altman', 'Harkirat Singh']
```

## Nested Tuples

```python
nested = (("ElonMusk", "Tesla"), ("Sam Altman", "OpenAI"), ("Sundar Pichai", "Google"))
print(nested[1][0])  # Output: Sam Altman
```

## Converting To and From Tuples

```python
# List to tuple
user_list = ["ElonMusk", "Sam Altman", "Harkirat Singh"]
user_tuple = tuple(user_list)

# Tuple to list
users = ("ElonMusk", "Sam Altman", "Harkirat Singh")
users_list = list(users)
users_list.append("Hitesh Choudhary")
users = tuple(users_list)  # Convert back to tuple
```

## When to Use Tuples vs Lists

**Use tuples when:**
1. You need an immutable sequence (values should not change)
2. You want to use the data as a dictionary key (lists cannot be dictionary keys)
3. You want to represent fixed collections like coordinates (x, y) or RGB colors
4. You need to ensure data integrity (prevent accidental modification)

**Use lists when:**
1. You need a mutable sequence (values may change)
2. You need to add or remove elements frequently
3. You need methods like append(), extend(), insert(), remove(), etc.

## Tuple Methods

Tuples have only two built-in methods due to their immutability:

1. `count()` - Returns the number of occurrences of a value
2. `index()` - Returns the index of the first occurrence of a value

## Named Tuples (collections module)

For more readable tuple-like objects, Python offers named tuples:

```python
from collections import namedtuple

# Define a named tuple type
Person = namedtuple('Person', ['name', 'age', 'job'])

# Create instances
elon = Person(name='Elon Musk', age=52, job='CEO')
sam = Person(name='Sam Altman', age=38, job='CEO')

# Access by name or index
print(elon.name)  # Output: Elon Musk
print(elon[0])    # Output: Elon Musk
```

## Performance Benefits

Tuples are generally more memory-efficient and faster than lists because they're immutable. Python can optimize certain operations with tuples that it cannot with lists.