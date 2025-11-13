# LIST BASICS

# Creating a list with different data types
sample_list = [42, 3.14, 'GPT-4', True]

# Another list with mixed data types
my_data = [1, 0.5, 'tokenizer', False]

# Creating empty lists
empty_list1 = []        # Using literal syntax
empty_list2 = list()    # Using the list() constructor

# Accessing list elements
print(my_data[0])   # Output: 1 (first element)
print(my_data[-1])  # Output: False (last element)

# IndexError example
# print(my_data[100])  # This would raise an IndexError

# Modifying a list element
my_data[2] = 'language model'
print(my_data)

# Adding an element to the list
my_data.append('NLP')  # Appends 'NLP' at the end of the list
print(my_data)

# Getting the length of the list
print(len(my_data))  # Output: 5

# Nested lists (2D lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element inside a nested list
print(matrix[1][2])  # Output: 6 (second row, third column)
