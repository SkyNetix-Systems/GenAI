# THE return STATEMENT

# RETURNING A VALUE FROM A BUILT-IN FUNCTION

# The `len()` function returns the length of a string
n = len('abc')
print(n)  # Output: 3

# RETURNING VALUES FROM FUNCTIONS

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# A function with no return statement (returns None implicitly)
def func():
    pass  # Placeholder function, does nothing

# UNREACHABLE CODE AFTER return

def example_function():
    """Demonstrates that code after `return` does not execute."""
    return 'This is the return value!'
    print('This line will never execute')  # This line is unreachable

# RETURNING MULTIPLE VALUES

def myfunc(x):
    """Returns multiple values: the input number, its square, and its cube."""
    return x, x**2, x**3  # Returns a tuple with three values

# Unpacking multiple returned values
a, b, c = myfunc(2)
print(a, b, c)  # Output: 2 4 8

# FUNCTION CALLS

# Storing the return value of `add()` in a variable
my_sum = add(10, 20)
print(my_sum)  # Output: 30

# Calling a function with no return value (returns None)
x = func()
print(x)  # Output: None

example_function()  # This function returns a value but is not printed
