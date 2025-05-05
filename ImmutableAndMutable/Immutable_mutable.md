# Mutable vs Immutable Types in Python

## Understanding Mutability in Python

In Python, understanding whether an object is **mutable** or **immutable** is crucial for predicting how your code will behave.

### Key Concept

- **Immutable**: Once created, the object's state/value cannot be modified. Any operation that appears to modify it actually creates a new object.
- **Mutable**: The object's state/value can be changed after creation without creating a new object.

## Memory References in Python

When you create a variable in Python, you're creating a reference (or name) that points to an object in memory:

```
variable_name = object_value
```

### Visual Representation of References:

```
# Memory diagram
┌────────────┐      ┌────────────┐
│ variable_x │─────›│  value_123 │
└────────────┘      └────────────┘
```

## Immutable Types in Python

### List of Immutable Types
1. Integers (`int`)
2. Floating point numbers (`float`)
3. Booleans (`bool`)
4. Strings (`str`)
5. Tuples (`tuple`)
6. Frozen sets (`frozenset`)
7. Bytes (`bytes`)

### How Immutability Works

Once an immutable object is created, its identity (memory location) and state cannot change. Any operation that seems to modify it actually creates a new object.

### Examples with Visual Representations:

#### Example 1: Integers

```python
x = 5  # Create integer object with value 5
y = x  # y now references the same object as x

# Memory representation:
# ┌────┐      ┌───┐
# │ x  │─────›│ 5 │
# └────┘      └───┘
#   ▲           
# ┌────┐        
# │ y  │────────┘
# └────┘        

print(id(x))  # Print memory address of x
print(id(y))  # Same as x

x = x + 1  # This creates a NEW integer object with value 6

# New memory representation:
# ┌────┐      ┌───┐
# │ x  │─────›│ 6 │
# └────┘      └───┘
#              
# ┌────┐      ┌───┐
# │ y  │─────›│ 5 │
# └────┘      └───┘

print(id(x))  # Different address now
print(id(y))  # Still points to original object
print(y)      # Still 5
```

#### Example 2: Strings

```python
name = "Python"
original_id = id(name)

# Memory representation:
# ┌──────┐      ┌────────┐
# │ name │─────›│"Python"│
# └──────┘      └────────┘

name = name + " Programming"  # Creates a new string object

# New memory representation:
# ┌──────┐      ┌───────────────────┐
# │ name │─────›│"Python Programming"│
# └──────┘      └───────────────────┘
#               
#               ┌────────┐
#               │"Python"│ (may be garbage collected if no other references)
#               └────────┘

print(id(name) == original_id)  # False - different object
```

#### Example 3: Tuples

```python
coordinates = (10, 20)

# Memory representation:
# ┌────────────┐      ┌────────┐
# │coordinates │─────›│(10, 20)│
# └────────────┘      └────────┘

# Try to modify - NOT POSSIBLE:
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Need to create a new tuple:
coordinates = (15, 20)  # New tuple object created

# New memory representation:
# ┌────────────┐      ┌────────┐
# │coordinates │─────›│(15, 20)│
# └────────────┘      └────────┘
#                      
#                     ┌────────┐
#                     │(10, 20)│ (may be garbage collected)
#                     └────────┘
```

#### Example 4: Immutable But Contains Mutable Elements

```python
# Tuple containing a list
t = (1, 2, [3, 4])

# Memory representation:
# ┌───┐      ┌─────────────┐
# │ t │─────›│(1, 2, [3,4])│
# └───┘      └─────────────┘
#                     │
#                     ▼
#                   ┌─────┐
#                   │[3,4]│
#                   └─────┘

# Cannot change the tuple structure:
# t[0] = 5  # TypeError

# But can modify the list inside the tuple:
t[2][0] = 30

# New memory representation:
# ┌───┐      ┌──────────────┐
# │ t │─────›│(1, 2, [30,4])│
# └───┘      └──────────────┘
#                     │
#                     ▼
#                   ┌──────┐
#                   │[30,4]│
#                   └──────┘

print(t)  # (1, 2, [30, 4])
```

## Mutable Types in Python

### List of Mutable Types
1. Lists (`list`)
2. Dictionaries (`dict`)
3. Sets (`set`)
4. Byte arrays (`bytearray`)
5. Arrays (`array.array`)
6. User-defined classes (by default)

### How Mutability Works

A mutable object can be modified after creation. Operations that modify the object change its internal state without creating a new object.

### Examples with Visual Representations:

#### Example 1: Lists

```python
numbers = [1, 2, 3]
numbers_copy = numbers  # Both variables reference the same list

# Memory representation:
# ┌─────────┐      ┌─────────┐
# │ numbers │─────›│[1, 2, 3]│
# └─────────┘      └─────────┘
#      ▲               
# ┌────────────┐        
# │numbers_copy│────────┘
# └────────────┘        

print(id(numbers))
print(id(numbers_copy))  # Same as numbers

numbers.append(4)  # Modifies the existing list

# Updated memory representation:
# ┌─────────┐      ┌───────────┐
# │ numbers │─────›│[1, 2, 3, 4]│
# └─────────┘      └───────────┘
#      ▲               
# ┌────────────┐        
# │numbers_copy│────────┘
# └────────────┘        

print(numbers)        # [1, 2, 3, 4]
print(numbers_copy)   # [1, 2, 3, 4] - also changed!
print(id(numbers) == id(numbers_copy))  # True - same object
```

#### Example 2: Dictionaries

```python
person = {"name": "John", "age": 30}
person_ref = person  # Both reference the same dictionary

# Memory representation:
# ┌────────┐      ┌─────────────────────┐
# │ person │─────›│{"name":"John","age":30}│
# └────────┘      └─────────────────────┘
#     ▲               
# ┌─────────────┐        
# │ person_ref  │────────┘
# └─────────────┘        

person["age"] = 31  # Modifies the existing dictionary

# Updated memory representation:
# ┌────────┐      ┌─────────────────────┐
# │ person │─────›│{"name":"John","age":31}│
# └────────┘      └─────────────────────┘
#     ▲               
# ┌─────────────┐        
# │ person_ref  │────────┘
# └─────────────┘        

print(person)       # {"name": "John", "age": 31}
print(person_ref)   # {"name": "John", "age": 31} - also changed!
```

#### Example 3: Sets

```python
fruits = {"apple", "banana", "cherry"}
fruits_alias = fruits  # Both reference the same set

# Memory representation:
# ┌────────┐      ┌─────────────────────────┐
# │ fruits │─────›│{"apple","banana","cherry"}│
# └────────┘      └─────────────────────────┘
#     ▲               
# ┌────────────┐        
# │fruits_alias│────────┘
# └────────────┘        

fruits.add("orange")  # Modifies the existing set

# Updated memory representation:
# ┌────────┐      ┌──────────────────────────────┐
# │ fruits │─────›│{"apple","banana","cherry","orange"}│
# └────────┘      └──────────────────────────────┘
#     ▲               
# ┌────────────┐        
# │fruits_alias│────────┘
# └────────────┘        

print(fruits)       # {"apple", "banana", "cherry", "orange"}
print(fruits_alias) # {"apple", "banana", "cherry", "orange"} - also changed
```

## Practical Implications

### 1. Function Arguments

```python
def modify_list(my_list):
    my_list.append(4)  # Modifies the original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # [1, 2, 3, 4] - Original list is modified!

def modify_string(my_string):
    my_string = my_string + " World"  # Creates a new string
    return my_string

greeting = "Hello"
result = modify_string(greeting)
print(greeting)  # "Hello" - Original string is unchanged
print(result)    # "Hello World" - New string returned
```

### 2. Creating Copies vs References

```python
# Reference (same object)
original_list = [1, 2, 3]
reference = original_list

# Shallow copy (new list, but same elements)
shallow_copy = original_list.copy()  # or list(original_list) or original_list[:]

# Deep copy (new list and new elements)
import copy
deep_copy = copy.deepcopy(original_list)

# Memory representation:
# ┌─────────────┐      ┌─────────┐
# │original_list│─────›│[1, 2, 3]│
# └─────────────┘      └─────────┘
#       ▲               
# ┌─────────┐        
# │reference│────────┘
# └─────────┘        
#
# ┌────────────┐      ┌─────────┐
# │shallow_copy│─────›│[1, 2, 3]│ (new list object but with references to the same elements)
# └────────────┘      └─────────┘
#
# ┌─────────┐      ┌─────────┐
# │deep_copy│─────›│[1, 2, 3]│ (completely new list and new element objects)
# └─────────┘      └─────────┘
```

## Tips for Working with Mutable/Immutable Types

1. **Be careful with function parameters**:
   - Mutable parameters can be modified within the function
   - Immutable parameters cannot be modified (but can be reassigned locally)

2. **Creating copies**:
   - Use `.copy()` or slice `[:]` for shallow copies of lists
   - Use `copy.deepcopy()` for deep copies of nested structures

3. **Comparing objects**:
   - `==` compares values
   - `is` compares identity (memory address)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same values)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```