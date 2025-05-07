# Python Dictionaries - Complete Guide

Dictionaries are key-value pairs in Python that allow you to store and retrieve data using unique keys.

## Creating Dictionaries

```python
# Creating a dictionary with key-value pairs
people = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 28,
    "Diana": 22
}

# Creating an empty dictionary
empty_dict = {}
```

## Accessing Dictionary Data

### Direct Access vs. get() Method

```python
people = {"Alice": 25, "Bob": 30, "Charlie": 28, "Diana": 22}

# Direct access using square brackets
print(people["Charlie"])  # Output: 28

# Using the get() method
print(people.get("Bob"))  # Output: 30

# The key difference: handling non-existent keys
# Direct access raises KeyError for non-existent keys
# people["Bab"]  # Raises KeyError: 'Bab'

# get() returns None for non-existent keys (or a default value)
print(people.get("Bab"))  # Output: None
print(people.get("Bab", "Not found"))  # Output: Not found
```

## Modifying Dictionaries

```python
people = {"Alice": 25, "Bob": 30, "Charlie": 28, "Diana": 22}

# Adding new key-value pairs
people["Dino"] = 21
print(people)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 28, 'Diana': 22, 'Dino': 21}

# Modifying existing values
people["Bob"] = 45
print(people)  # Output: {'Alice': 25, 'Bob': 45, 'Charlie': 28, 'Diana': 22, 'Dino': 21}
```

## Iterating Through Dictionaries

```python
people = {"Alice": 25, "Bob": 45, "Charlie": 28, "Diana": 22}

# Iterating through keys (default)
for key in people:
    print(key)  # Output: Alice, Bob, Charlie, Diana

# Accessing values through keys
for key in people:
    print(key, people[key])  # Output: Alice 25, Bob 45, Charlie 28, Diana 22

# Using items() to get both key and value
for key, value in people.items():
    print(key, value)  # Output: Alice 25, Bob 45, Charlie 28, Diana 22
```

> **Note**: Unlike lists where iteration gives values, dictionary iteration gives keys by default. Use `.items()` to get both keys and values.

## Dictionary Operations

### Checking if a Key Exists

```python
people = {"Alice": 25, "Bob": 45, "Charlie": 28, "Diana": 22}

if "Alice" in people:
    print("Alice is in the dictionary.")  # Output: Alice is in the dictionary.
```

### Getting Dictionary Length

```python
people = {"Alice": 25, "Bob": 45, "Charlie": 28, "Diana": 22}

print(len(people))  # Output: 4
```

## Removing Items from a Dictionary

```python
people = {"Alice": 25, "Bob": 45, "Charlie": 28, "Diana": 22, "Dino": 21}

# pop() removes a specific key and returns its value
# Note: Unlike lists, dictionaries require a key for pop()
age = people.pop("Dino")
print(age)  # Output: 21
print(people)  # Output: {'Alice': 25, 'Bob': 45, 'Charlie': 28, 'Diana': 22}

# popitem() removes and returns the last inserted key-value pair as a tuple
last_item = people.popitem()
print(last_item)  # Output: ('Diana', 22)
print(people)  # Output: {'Alice': 25, 'Bob': 45, 'Charlie': 28}

# del statement removes a specific key
del people["Charlie"]
print(people)  # Output: {'Alice': 25, 'Bob': 45}

# clear() removes all items
people.clear()
print(people)  # Output: {}
```

## Dictionary Copies vs. References

```python
people = {"Alice": 25, "Bob": 45, "Charlie": 28}

# Creating a reference (changes to one affect the other)
people_ref = people

# Creating a new copy (changes to one don't affect the other)
people_copy = people.copy()
people_copy["Carlos"] = 20

print(people_copy)  # Output: {'Alice': 25, 'Bob': 45, 'Charlie': 28, 'Carlos': 20}
print(people)  # Output: {'Alice': 25, 'Bob': 45, 'Charlie': 28}
```

## Nested Dictionaries

```python
people = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "London"},
    "Charlie": {"age": 28, "city": "Paris"},
    "Diana": {"age": 22, "city": "Tokyo"}
}

# Accessing nested dictionary values
print(people["Bob"]["city"])  # Output: London
```

## Dictionary Comprehension

```python
# Create a dictionary of numbers and their squares
squared_num = {x: x**2 for x in range(10)}
print(squared_num)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## Dictionary Methods

```python
# Using dict.fromkeys() - Simple example with single value
subjects = ["Math", "Science", "History"]
grades = dict.fromkeys(subjects, 0)
print(grades)  # Output: {'Math': 0, 'Science': 0, 'History': 0}

# Be careful with mutable default values
keys = ["team1", "team2"]
empty_scores = dict.fromkeys(keys, [])
print(empty_scores)  # Output: {'team1': [], 'team2': []}

# Warning: All keys reference the same list!
empty_scores["team1"].append(3)
print(empty_scores)  # Output: {'team1': [3], 'team2': [3]} - Both lists changed!

# Better approach for mutable defaults
better_scores = {key: [] for key in keys}
better_scores["team1"].append(3)
print(better_scores)  # Output: {'team1': [3], 'team2': []}

# Other useful methods
people = {"Alice": 25, "Bob": 45, "Charlie": 28}

# Get all keys as a view object
keys = people.keys()
print(list(keys))  # Output: ['Alice', 'Bob', 'Charlie']

# Get all values as a view object
values = people.values()
print(list(values))  # Output: [25, 45, 28]

# Update dictionary with another dictionary
people.update({"Diana": 22, "Alice": 26})
print(people)  # Output: {'Alice': 26, 'Bob': 45, 'Charlie': 28, 'Diana': 22}
```

## Lists vs. Dictionaries

| Feature | List | Dictionary |
|---------|------|------------|
| Access | Index-based (people[0]) | Key-based (people["Alice"]) |
| Order | Ordered sequence | Maintains insertion order (Python 3.7+) |
| Insertion | Can insert at any index | Cannot insert at specific position |
| Iteration | Default gives values | Default gives keys |
| Lookup Speed | O(n) for value lookup | O(1) for key lookup |
| Use Case | Ordered collection of items | When you need key-value mapping |