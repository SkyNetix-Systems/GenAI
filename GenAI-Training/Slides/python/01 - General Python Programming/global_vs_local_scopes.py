# GLOBAL vs. LOCAL SCOPES

# GLOBAL VARIABLE
accuracy = 0.85  # Defined in the global scope

def update_accuracy():
    """Updates the global variable `accuracy` inside the function."""
    global accuracy  # Declaring accuracy as global to modify it
    accuracy = 0.9  # Updating the global variable
    print(f'Updated accuracy inside function: {accuracy}')

# Function call modifies the global variable
update_accuracy()
print(f'Accuracy outside function: {accuracy}')

# LOCAL VARIABLE (No Effect on Global Scope)

def calculate_sum(values):
    """Demonstrates local scope by printing the passed argument."""
    print(values)  # `values` exists only within this function

calculate_sum([1, 2, 3])
