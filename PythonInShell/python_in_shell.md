# Python in the Shell

## Interactive Python Shell

### Starting the Python Shell
To open the Python interactive shell:
```
python
```
or 
```
python3
```
(depending on your system)

You'll see something like:
```
Python 3.9.5 (default, May 4 2021, 03:36:27) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the prompt where you can type Python commands.

### Basic Usage

#### Executing Simple Commands
```python
>>> print("Hello World")
Hello World

>>> 2 + 2
4
```

#### Using Variables
```python
>>> x = 10
>>> y = 20
>>> x + y
30
```

#### Using Variables
```python
>>> 'hello'
'hello'
>>> 'this is a test'
'this is a test'
>>> 

>>> "hello" + "world"
'helloworld'
>>> "hello" * 3
'hellohellohello'
>>> 

>>> "strings can contain # characters"
'strings can contain # characters'
>>> 
```
Note that a # inside a string doesn't create a comment.

#### Multiline Statements
For code blocks like loops or functions, the shell will show a secondary prompt (`...`) for continuation lines:
```python
>>> def greet(name):
...     return "Hello, " + name
... 
>>> greet("Python User")
'Hello, Python User'
```

### Helpful Features

#### Command History
- Use the up/down arrow keys to navigate through previous commands
- Press Enter to execute a previous command

#### Auto-completion
- Press Tab to auto-complete variable names, functions, etc.
```python
>>> import ran[TAB]  # Completes to "random"
```

#### Help System
```python
>>> help()  # Enter interactive help
>>> help(print)  # Get help on a specific function
>>> help("modules")  # List all available modules
```

#### Quitting the Shell
```python
>>> exit()
```
or
```python
>>> quit()
```
or press Ctrl+D (on Unix/Mac) or Ctrl+Z followed by Enter (on Windows)

# Python Import and System Commands

## System Information and Navigation

### `import sys` - System-specific Parameters and Functions

```python
# Get the platform identifier
import sys
sys.platform  # Returns platform identifier, e.g., 'win32', 'darwin', 'linux'

# Get Python version
sys.version  # Returns Python version string

# Command line arguments
sys.argv  # List of command line arguments passed to the Python script

# Module search path
sys.path  # List of directories Python searches for modules

# Exit a program
sys.exit()  # Exit the program (optional exit code as parameter)
```

### `import os` - Operating System Interface

```python
# Get current working directory
import os
os.getcwd()  # Returns the current working directory as a string

# Change directory
os.chdir('/path/to/directory')  # Changes the current working directory

# List files and directories
os.listdir()  # Lists files and directories in current directory
os.listdir('/path/to/directory')  # Lists files and directories in specified path

# Create a directory
os.mkdir('new_directory')  # Creates a new directory

# Remove a file
os.remove('filename.txt')  # Removes the specified file

# Environment variables
os.environ  # Dictionary of environment variables
os.environ['HOME']  # Access specific environment variable
```

## Module Imports and Reloading

### Basic Import Commands

```python
# Import a module (runs the code in the module)
import math
math.sqrt(16)  # Using a function from imported module

# Import with alias
import numpy as np
np.array([1, 2, 3])  # Using the alias

# Import specific items from a module
from math import sqrt, pi
sqrt(16)  # Directly use the imported function (no math. prefix needed)

# Import all items from a module (not recommended in production code)
from math import *
cos(pi)  # Directly use any function from math
```

### Importing Your Own Files

```python
# If you have a file named mymodule.py in the same directory:
import mymodule  # This executes the file and makes its contents available

# If your file is in a subdirectory:
import subdirectory.mymodule

# If you want specific functions:
from mymodule import my_function
```

### Reloading Modules

When you modify a module's source code, Python doesn't automatically reload it. You need to use `reload()`:

```python
# First import
import mymodule

# After changing mymodule.py, reload it:
from importlib import reload
reload(mymodule)  # This reloads the updated module
```

### Package Management

```python
# Show installed packages
import pip
pip.main(['list'])  # In newer versions, use: pip._internal.main(['list'])

# Import a package that might not be installed
try:
    import pandas as pd
except ImportError:
    print("pandas is not installed")
```
