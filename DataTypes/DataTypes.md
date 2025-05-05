# Python Data Types

## Basic Data Types

### 1. Integers (`int`)
Whole numbers without decimal points.

```python
# Integer examples
age = 25
temperature = -10
count = 0

# Large integers
population = 7_800_000_000  # Underscores for readability

# Type checking
print(type(age))  # <class 'int'>
```

### 2. Floating Point Numbers (`float`)
Numbers with decimal points.

```python
# Float examples
height = 5.11
pi = 3.14159
temperature = -2.5

# Scientific notation
distance = 1.5e8  # 150,000,000
tiny = 1e-9       # 0.000000001

print(type(height))  # <class 'float'>
```

### 3. Strings (`str`)
Text enclosed in quotes (single, double, or triple quotes).

```python
# String examples
name = "John"
message = 'Hello, World!'
address = "123 Main St."

# Multi-line strings with triple quotes
description = """This is a longer
description that spans
multiple lines."""

# String operations
full_name = "John" + " " + "Doe"  # Concatenation
greeting = "Hello" * 3  # Repetition: "HelloHelloHello"

# Accessing characters (indexing)
first_letter = name[0]  # 'J'
last_letter = name[-1]  # 'n'

# Slicing
substring = message[0:5]  # 'Hello'

print(type(name))  # <class 'str'>
```

### 4. Booleans (`bool`)
True or False values.

```python
# Boolean examples
is_active = True
has_permission = False

# Boolean from comparisons
is_adult = age >= 18  # True if age is 18 or more
is_valid = password == "secret"  # True if password equals "secret"

# Boolean operations
can_access = is_active and has_permission  # AND
need_attention = is_urgent or is_important  # OR
is_pending = not is_completed  # NOT

print(type(is_active))  # <class 'bool'>
```

### 5. None Type (`NoneType`)
Represents absence of value or null value.

```python
# None examples
result = None
default_value = None

# Common usage
def function_without_return():
    pass  # Do something but don't return a value

output = function_without_return()  # output will be None

# Checking for None
if result is None:
    print("No result yet")

print(type(None))  # <class 'NoneType'>
```

## Collection Data Types

### 1. Lists (`list`)
Ordered, mutable collections of items.

```python
# List examples
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
nested = [1, [2, 3], [4, 5, 6]]
empty_list = []

# Accessing elements
first_fruit = fruits[0]  # "apple"
last_number = numbers[-1]  # 5
sub_list = numbers[1:4]  # [2, 3, 4]

# Modifying lists
fruits.append("orange")  # Add to end: ["apple", "banana", "cherry", "orange"]
fruits.insert(1, "mango")  # Insert at position: ["apple", "mango", "banana", "cherry", "orange"]
fruits.remove("banana")  # Remove item: ["apple", "mango", "cherry", "orange"]
popped = fruits.pop()  # Remove & return last item: "orange"

# List operations
combined = fruits + ["grape", "kiwi"]  # Concatenation
doubled = numbers * 2  # Repetition: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
length = len(fruits)  # Number of items

print(type(fruits))  # <class 'list'>
```

### 2. Tuples (`tuple`)
Ordered, immutable collections of items.

```python
# Tuple examples
coordinates = (10, 20)
rgb_color = (255, 0, 128)
single_item = (42,)  # Comma needed for single-item tuple
empty_tuple = ()
mixed_tuple = (1, "hello", True)

# Tuple from other sequences
tuple_from_list = tuple([1, 2, 3])
chars = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

# Accessing elements (similar to lists)
x_coord = coordinates[0]  # 10
last = rgb_color[-1]  # 128

# Cannot modify tuples
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Tuple operations
combined = coordinates + (30, 40)  # (10, 20, 30, 40)
repeated = coordinates * 3  # (10, 20, 10, 20, 10, 20)

print(type(coordinates))  # <class 'tuple'>
```

### 3. Dictionaries (`dict`)
Unordered collections of key-value pairs.

```python
# Dictionary examples
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Different key types
mix_keys = {
    42: "answer",
    True: "boolean key",
    (1, 2): "tuple key"  # Immutable keys only
}

# Empty dictionary
empty_dict = {}

# Accessing values
name = person["name"]  # "John"
age = person.get("age")  # 30
# Safe access with default
country = person.get("country", "Unknown")  # "Unknown"

# Modifying dictionaries
person["email"] = "john@example.com"  # Add new key-value
person["age"] = 31  # Modify existing value
del person["city"]  # Remove key-value pair
popped = person.pop("email")  # Remove & return value

# Dictionary operations
keys = person.keys()  # Dict keys view
values = person.values()  # Dict values view
items = person.items()  # Dict items view (key-value tuples)

print(type(person))  # <class 'dict'>
```

### 4. Sets (`set`)
Unordered collections of unique items.

```python
# Set examples
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", (1, 2, 3)}  # Only immutable items
# empty_set = {}  # Wrong! This creates an empty dict
empty_set = set()  # Correct way to create empty set

# Set from other sequences
vowels = set("aeiou")  # {'a', 'e', 'i', 'o', 'u'}
unique_nums = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Modifying sets
fruits.add("orange")  # Add single item
fruits.update(["mango", "grape"])  # Add multiple items
fruits.remove("banana")  # Remove item (raises error if not found)
fruits.discard("kiwi")  # Remove if present (no error if not found)
popped = fruits.pop()  # Remove and return arbitrary item

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b  # {1, 2, 3, 4, 5, 6}
intersection = a & b  # {3, 4}
difference = a - b  # {1, 2}
symmetric_diff = a ^ b  # {1, 2, 5, 6}

print(type(fruits))  # <class 'set'>
```

### 5. Frozen Sets (`frozenset`)
Immutable version of sets.

```python
# Frozenset examples
vowels = frozenset({"a", "e", "i", "o", "u"})
numbers = frozenset([1, 2, 3, 4, 5])

# Cannot be modified
# vowels.add("y")  # AttributeError: 'frozenset' object has no attribute 'add'

# Set operations still work
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
union = a | b  # frozenset({1, 2, 3, 4, 5, 6})
intersection = a & b  # frozenset({3, 4})

print(type(vowels))  # <class 'frozenset'>
```


## Type Conversion

```python
# String to number
age_str = "25"
age_int = int(age_str)  # 25
price_str = "19.99"
price_float = float(price_str)  # 19.99

# Number to string
count = 42
count_str = str(count)  # "42"

# Between collections
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)  # (1, 2, 3, 4)
my_set = set(my_list)  # {1, 2, 3, 4}
back_to_list = list(my_set)  # [1, 2, 3, 4] (order may differ)

# Dictionary conversions
items = [("name", "John"), ("age", 30)]
dict_from_items = dict(items)  # {"name": "John", "age": 30}
```