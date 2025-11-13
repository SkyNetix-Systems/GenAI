# VARIABLE SCOPE AND NAMESPACES

# BUILT-IN NAMESPACE EXAMPLE

# The `max` function is part of Python's built-in namespace
scores = [85, 90, 78, 92]
print(max(scores))  # Output: 92

# GLOBAL NAMESPACE EXAMPLE

# A global variable defined at the module level
accuracy = 0.95

def report_accuracy():
    """Prints the accuracy of the model in percentage."""
    print(f'Model accuracy is {accuracy * 100}%')

report_accuracy()  # Output: Model accuracy is 95.0%

# LOCAL NAMESPACE EXAMPLE

def count_tokens(text):
    """Returns the number of words (tokens) in a given text."""
    tokens = len(text.split())  # `tokens` exists only within this function
    return tokens

print(count_tokens('Python makes AI so accessible!'))  # Output: 5

# Uncommenting the following line would cause a NameError because `tokens` is local to count_tokens()
# print(tokens)  # NameError: name 'tokens' is not defined
