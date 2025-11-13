# FUNCTION VARIABLE-LENGTH ARGUMENTS: *args, **kwargs

# USING *args (ARBITRARY POSITIONAL ARGUMENTS)

def calculate_total_cost(base_cost, *args):
    """Calculates the total cost by adding additional variable costs."""
    print(args)  # Displays *args as a tuple of additional costs
    return base_cost + sum(args)

# Function calls with different numbers of additional arguments
print(calculate_total_cost(10, 5, 2, 6, 7))  # Output: 30
print(calculate_total_cost(5, 9))            # Output: 14

# USING *args TO CREATE HASHTAGS

def create_hashtags(*tags):
    """Creates a space-separated hashtag string from multiple hashtag inputs."""
    return ' '.join(tags)

# Example of hashtag creation
print(create_hashtags('#AI', '#Python', '#GenAI', '#LLMs'))
# Output: '#AI #Python #GenAI #LLMs'


# USING **kwargs (ARBITRARY KEYWORD ARGUMENTS)

def display_user_info(**user_data):
    """Displays user information using keyword arguments."""
    for key, value in user_data.items():
        print(f'{key} => {value}')

# Function call with multiple named arguments
display_user_info(name='Alice', age=30, membership='Premium')
# Output:
# name => Alice
# age => 30
# membership => Premium
