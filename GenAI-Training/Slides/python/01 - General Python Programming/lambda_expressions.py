# LAMBDA EXPRESSIONS

# Syntax:
# lambda parameters: expression

# Regular function equivalent
def add(a, b, c):
    """Returns the sum of three numbers."""
    return a + b + c

# Lambda expression equivalent
s = (lambda a, b, c: a + b + c)(3, 4, 5)  # Directly calling the lambda function
print(s)  # Output: 12

# Lambda function with a default parameter
square = lambda x=10: x ** 2
print(square(4))   # Output: 16 (4 squared)
print(square())    # Output: 100 (default value 10 squared)

# Using lambda with the sort() method
friends = [('Diana', 30), ('Ana', 25), ('Tudor fdafdafdasf', 22)]

# Sorting by age (second element in tuple)
friends.sort(key=lambda x: x[1])
print(friends)  # Sorted list based on age

# Sorting by name length
friends.sort(key=lambda x: len(x[0]))
print(friends)  # Sorted list based on the length of names
