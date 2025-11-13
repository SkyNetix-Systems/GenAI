# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

message = 'GenAIis amazing!'

# INDEXING: Accessing individual characters in a string
print(message[0])    # First character: 'G'
print(message[5])    # Sixth character: 'i'
print(message[-1])   # Last character: '!'
print(message[-7])   # Seventh character from the end: 'a'

# Get the length of the string
n = len(message)
print(n)             # Output: 16 (total characters in 'GenAIis amazing!')

# Access the last character using length
print(message[n-1])  # Equivalent to message[-1]

# STRINGS ARE IMMUTABLE
# message[0] = 'X'  # Uncommenting this line will cause an error

# STRING CONCATENATION

greeting = 'Hello, '
role = 'AI enthusiast'

# Combining strings using `+`
print(greeting + role + '!')  # Output: 'Hello, AI enthusiast!'

# Concatenating strings with different data types (requires type conversion)
print('Version ' + str(4.0))  # Output: 'Version 4.0'

# STRING REPETITION

separator = '🤖'

# Repeating a string multiple times
print(separator * 5)  # Output: '🤖🤖🤖🤖🤖'

# STRING SLICING

tech = 'Machine Learning'

# Extracting a substring using slicing: string[start:stop]
print(tech[0:7])   # 'Machine' (characters from index 0 to 6)

# Demonstrating different slicing variations

# string[start:stop:step]

print(tech[:7])    # 'Machine' (from the start up to index 6)
print(tech[8:])    # 'Learning' (from index 8 to the end)
print(tech[-4:])   # 'ning' (last four characters)
print(tech[8:100]) # 'Learning' (Python doesn't throw an error if stop exceeds length)
print(tech[0:14:2])# 'McieLann' (every second character)
print(tech[::-1])  # 'gninraeL enihcaM' (reversed string)
