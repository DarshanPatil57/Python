# Python Strings - Comprehensive Notes

## String Basics

A string in Python is a sequence of characters enclosed in quotes (single, double, or triple quotes).

```python
# Creating strings
name = 'John'             # Single quotes
name = "John"             # Double quotes
description = """This is  
a multi-line
string"""                 # Triple quotes for multi-line strings
```

## String Indexing and Slicing

Strings can be accessed by index (starting from 0) or sliced to get substrings.

```python
# Indexing (accessing individual characters)
user = "John"
first_char = user[0]      # 'J'
last_char = user[-1]      # 'n'

# Slicing (getting substrings)
# Format: string[start:end:step]
# Note: end index is exclusive

slice_user = user[0:2]    # 'Jo' (characters at index 0 and 1)
num_list = "0123456789"

# Slicing variations
num_list[3:]              # '3456789' (from index 3 to end)
num_list[:]               # '0123456789' (entire string)
num_list[:7]              # '0123456' (from start to index 6)
num_list[0:7:2]           # '0246' (from index 0 to 6, stepping by 2)
num_list[0:8:-4]          # '' (empty - negative step requires proper direction)
num_list[8:0:-1]          # '987654321' (backwards, from index 8 to 1)
```

## String Methods

Python strings come with many built-in methods for manipulation and analysis.

### Case Conversion
```python
user = "John"
user.lower()              # 'john' (all lowercase)
user.upper()              # 'JOHN' (all uppercase)
user.capitalize()         # 'John' (first letter capitalized)
user.title()              # 'John' (first letter of each word capitalized)
user.swapcase()           # 'jOHN' (swap case of each letter)
```

### Whitespace Handling
```python
user = "  John Doe  "
user.strip()              # 'John Doe' (removes leading/trailing spaces)
user.lstrip()             # 'John Doe  ' (removes leading spaces)
user.rstrip()             # '  John Doe' (removes trailing spaces)
```

### Finding and Replacing
```python
users = "John, ElonMusk, Sam Altman, Bill Gate"
users.find("Sam")         # 16 (index of first occurrence)
users.find("sam")         # -1 (not found - case sensitive)
users.rfind("a")          # 33 (index of last occurrence)
users.count("a")          # 3 (count occurrences)

# Replace content
user = "  John Doe  "
user.replace("John", "Sam")  # '  Sam Doe  ' (replaces all occurrences)
user.replace("o", "X", 1)    # '  JXhn Doe  ' (replace with count limit)
```

### Splitting and Joining
```python
# Splitting strings
users = "John, ElonMusk, Sam Altman, Bill Gate"
users.split(", ")         # ['John', 'ElonMusk', 'Sam Altman', 'Bill Gate']

# Common splitting patterns
text = "Hello\nWorld"
text.splitlines()         # ['Hello', 'World'] (split by newlines)
path = "/home/user/documents"
path.split("/")           # ['', 'home', 'user', 'documents']

# Joining strings
data = ["Ronaldo", "Messi", "Neymar"]
" ".join(data)            # 'Ronaldo Messi Neymar'
", ".join(data)           # 'Ronaldo, Messi, Neymar'
"".join(data)             # 'RonaldoMessiNeymar'
```

### String Formatting

#### Format Method
```python
name = 'John Doe'
age = 21
info = "My name is {} and my age is {} ."
info.format(name, age)    # 'My name is John Doe and my age is 21 .'

# Format with positional arguments
"The {1} ate the {0}".format("mouse", "cat")  # 'The cat ate the mouse'

# Format with named parameters
"{name} is {age} years old".format(name="John", age=21)
```

#### F-strings (Python 3.6+)
```python
name = 'John Doe'
age = 21
f"My name is {name} and my age is {age}."  # 'My name is John Doe and my age is 21.'

# Expressions in f-strings
f"2 + 2 = {2 + 2}"        # '2 + 2 = 4'
f"Uppercase: {name.upper()}"  # 'Uppercase: JOHN DOE'
```

#### %-formatting (older style)
```python
name = 'John Doe'
age = 21
"My name is %s and my age is %d." % (name, age)  # 'My name is John Doe and my age is 21.'
```

### Checking String Content
```python
# Character type checks
"abc123".isalnum()        # True (only alphanumeric)
"abc".isalpha()           # True (only alphabetic)
"123".isdigit()           # True (only digits)
"abc".islower()           # True (all lowercase)
"ABC".isupper()           # True (all uppercase)
"Hello World".istitle()   # True (title case)
"   ".isspace()           # True (only whitespace)

# Starting and ending checks
"Hello".startswith("He")  # True
"Hello".endswith("lo")    # True
```

## String Iteration

Strings can be iterated character by character.

```python
user = 'John Doe'
for letter in user:
    print(letter)
# Output:
# J
# o
# h
# n
# 
# D
# o
# e
```

## String Concatenation

Strings can be combined in various ways.

```python
first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name  # 'John Doe'

# Using join method
full_name = " ".join([first_name, last_name])  # 'John Doe'

# Using format method
full_name = "{} {}".format(first_name, last_name)  # 'John Doe'

# Using f-strings (Python 3.6+)
full_name = f"{first_name} {last_name}"  # 'John Doe'
```

## Escape Characters

Special characters can be represented using escape sequences.

```python
print("Line1\nLine2")     # Newline
print("Tab\tSpace")       # Tab
print("Quote: \"Hello\"") # Quote character
print("Path: C:\\Users")  # Backslash
print("Bell: \a")         # Bell sound (ASCII 7)
```

## Raw Strings

Raw strings ignore escape characters.

```python
print(r"C:\Users\name")   # Prints literally as C:\Users\name
```

## String Methods Reference

| Method | Description |
|--------|-------------|
| `str.capitalize()` | Returns a copy with first character capitalized |
| `str.casefold()` | Returns a lowercase string (more aggressive than lower()) |
| `str.center(width)` | Returns centered string padded with spaces |
| `str.count(sub)` | Counts occurrences of substring |
| `str.encode()` | Returns encoded string as bytes object |
| `str.endswith(suffix)` | Returns True if string ends with suffix |
| `str.expandtabs()` | Replaces tabs with spaces |
| `str.find(sub)` | Returns lowest index of substring or -1 |
| `str.format()` | Formats string with specified values |
| `str.index(sub)` | Like find() but raises ValueError if not found |
| `str.isalnum()` | Returns True if all chars are alphanumeric |
| `str.isalpha()` | Returns True if all chars are alphabetic |
| `str.isascii()` | Returns True if all chars are ASCII |
| `str.isdecimal()` | Returns True if all chars are decimal |
| `str.isdigit()` | Returns True if all chars are digits |
| `str.isidentifier()` | Returns True if valid identifier |
| `str.islower()` | Returns True if all chars are lowercase |
| `str.isnumeric()` | Returns True if all chars are numeric |
| `str.isprintable()` | Returns True if all chars are printable |
| `str.isspace()` | Returns True if all chars are whitespace |
| `str.istitle()` | Returns True if string is titlecased |
| `str.isupper()` | Returns True if all chars are uppercase |
| `str.join(iterable)` | Joins elements of iterable with string as separator |
| `str.ljust(width)` | Left-aligns string in field of given width |
| `str.lower()` | Returns lowercase string |
| `str.lstrip()` | Removes leading whitespace |
| `str.partition(sep)` | Partitions string at first occurrence of separator |
| `str.replace(old, new)` | Replaces occurrences of substring |
| `str.rfind(sub)` | Returns highest index of substring or -1 |
| `str.rindex(sub)` | Like rfind() but raises ValueError if not found |
| `str.rjust(width)` | Right-aligns string in field of given width |
| `str.rpartition(sep)` | Partitions string at last occurrence of separator |
| `str.rsplit(sep)` | Splits string from right by separator |
| `str.rstrip()` | Removes trailing whitespace |
| `str.split(sep)` | Splits string by separator |
| `str.splitlines()` | Splits string at line breaks |
| `str.startswith(prefix)` | Returns True if string starts with prefix |
| `str.strip()` | Removes leading and trailing whitespace |
| `str.swapcase()` | Swaps case of all characters |
| `str.title()` | Returns titlecased string |
| `str.translate(table)` | Returns string mapped through translation table |
| `str.upper()` | Returns uppercase string |
| `str.zfill(width)` | Pads string with zeros on the left |


