#8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, country="India")


# **kwargs collects all keyword arguments into a dictionary
# .items() lets you loop through the dictionary to get each key: value pair.

