# TUPLE BASICS

# Defining a tuple with geographical coordinates
location = (37.7749, -122.4194)  # SF coordinates

# Creating empty tuples using two different methods
empty_tuple1 = tuple()
empty_tuple2 = ()

# A single-element tuple requires a trailing comma
single = (10,)      # This is a tuple
not_a_tuple = (10)  # This is an integer, not a tuple

# Converting lists and strings to tuples
nums = tuple([1, 2, 3])     # Creates a tuple from a list
letters = tuple('hello')    # Creates a tuple from a string

# Accessing tuple elements using indexing
print(location[0])  # Output: 37.7749

# TUPLE UNPACKING

# Assigning tuple values to variables
coordinates = (37.7749, -122.4194)
latitude, longitude = coordinates   # Tuple unpacking
print(latitude, longitude)          # Output: 37.7749 -122.4194

# NESTED TUPLES

# Defining a matrix using nested tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (67, 8, 9)
)

# Accessing elements in a nested tuple
print(matrix[1][0])  # Output: 4 (First element of the second tuple)

# Tuples are immutable, the following line would cause an error:
# coordinates[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Checking for tuple membership using `in`
if (1, 2, 3) in matrix:
    print('found!')  # Output: found!
