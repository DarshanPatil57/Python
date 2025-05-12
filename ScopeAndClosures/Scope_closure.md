# Python Scopes and Closures

## Variable Scope in Python

### Local Scope
- Variables defined within a function exist only inside that function
- Cannot be accessed from outside the function
- Created when the function is called and destroyed when the function exits

```python
def my_function():
    x = 10  # Local variable
    print(x)  # Works fine

my_function()  # Outputs: 10
# print(x)  # Would raise a NameError: name 'x' is not defined
```

### Global Scope
- Variables defined outside of any function
- Accessible throughout the file, including inside functions (for reading)
- Need the `global` keyword to modify from within a function

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can access (read) global variable

my_function()  # Outputs: 10

def modify_global():
    global x  # Declare intention to modify global x
    x = 20

modify_global()
print(x)  # Outputs: 20
```

### Enclosing (Nonlocal) Scope
- Relevant for nested functions
- Inner functions can access variables from outer functions
- Use `nonlocal` keyword to modify outer function variables

```python
def outer_function():
    y = 20  # Enclosing variable
    
    def inner_function():
        print(y)  # Can access outer function's variable
    
    inner_function()

outer_function()  # Outputs: 20
```

### Built-in Scope
- Python's pre-defined functions and keywords (like `print`, `len`, etc.)
- Always available in any Python program

## The LEGB Rule

Python follows the LEGB rule for variable lookup:
1. **L**ocal: Variables defined within the current function
2. **E**nclosing: Variables in the local scope of enclosing functions
3. **G**lobal: Variables defined at the top level of a module
4. **B**uilt-in: Python's pre-defined names

## Closures in Python

A closure is a function object that remembers values in the enclosing scope even if they are not present in memory.

### Key Characteristics of Closures:
- A nested function that references variables from its enclosing scope
- The enclosing function returns the nested function
- The enclosed variables are "remembered" even after the outer function exits

### Basic Closure Example:

```python
def make_multiplier(x):
    def multiply(y):
        return x * y  # x is from the enclosing scope
    return multiply  # Return the inner function

# Create closure functions
double = make_multiplier(2)
triple = make_multiplier(3)

# Use closure functions
print(double(5))  # Outputs: 10
print(triple(5))  # Outputs: 15
```

### Real-world Usage Example:

```python
def create_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
        
    return increment

counter = create_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## Benefits of Closures

1. **Data Encapsulation**: Hide data from the global scope
2. **State Preservation**: Maintain state between function calls
3. **Function Factories**: Create specialized functions dynamically
4. **Callback Functions**: Store context for later execution

## Common Pitfalls

### Late Binding Closures
When using loops with closures, be careful of late binding:

```python
# This doesn't work as expected
def create_functions():
    functions = []
    for i in range(3):
        def func():
            return i  # i will be 2 for all functions!
        functions.append(func)
    return functions

# Solution: Use default parameters
def create_functions_fixed():
    functions = []
    for i in range(3):
        def func(i=i):  # Capture current value of i
            return i
        functions.append(func)
    return functions
```

## Practical Applications

1. **Decorators**: Functions that modify other functions
2. **Context Managers**: Control resource acquisition and release
3. **Event Handlers**: Store context for callback execution
4. **Memoization**: Cache function results for repeated calls

Remember that while closures are powerful, they should be used judiciously as they can make code harder to understand if overused.