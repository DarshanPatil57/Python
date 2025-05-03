# Python Inner Workings - Simplified

## How Python Works Behind the Scenes

### 1. Interpretation Process
Python is an interpreted language, which means code is executed line by line:

1. You write code in a `.py` file
2. The Python interpreter reads your code
3. The interpreter converts each line to bytecode [BYTE-CODE IS : low-level & Platform Independent]

    =>Byte code runs faster
    =>pyc is compiled python (__pycache__)

4. The Python Virtual Machine (PVM) executes the bytecode

    Python Virtual Machine (PVM): 
    -also known as python interpreter
    -run time engine
    -code loop to iterate byte code

    =>NOTE: Byte code is not machine code

Think of it like a translator who reads your instructions and carries them out immediately.

### 2. Python's Memory Management

#### Objects and References
- Everything in Python is an object (numbers, strings, functions, etc.)
- Variables are just names pointing to objects
- When you write `x = 5`, you create an integer object with value 5 and name it `x`

```python
a = 10  # Create object 10, name it 'a'
b = a   # 'b' now points to the same object as 'a'
```

#### Automatic Memory Management
Python handles memory for you:
- **Allocation**: Python automatically creates objects when needed
- **Garbage Collection**: Python automatically removes objects when they're no longer used

This means you don't need to manually free memory like in C/C++.

### 3. Function Execution

When you call a function, Python:
1. Creates a new local namespace (for variables inside the function)
2. Executes the function code
3. Returns to the previous point in your program

```python
def greet(name):  # Creates function object
    message = "Hello, " + name  # Local variable
    print(message)
    
greet("John")  # Function called, executes, then returns
```

### 4. Python's Execution Model

#### Namespaces
A namespace is like a container for variables:
- **Local**: Inside functions
- **Global**: At the file level
- **Built-in**: Python's pre-defined items

Python searches for names in this order (local → global → built-in).

#### Object Lifetime
1. Object is created when code is first executed
2. Object lives as long as there's at least one reference to it
3. Object is deleted when no references remain
