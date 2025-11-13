# PYTHON FUNCTIONS

def my_function():
    print('Hello Python World!')
    x = 10
    print(x ** x)

def say_hello(name):
    """Prints a greeting message with the provided name."""
    print(f'Hello {name}!')

# Uncomment the line below to call my_function
my_function()


# 1. Using the help() function to display the docstring of say_hello
help(say_hello)

# 2. Accessing the __doc__ attribute directly
print(say_hello.__doc__)
