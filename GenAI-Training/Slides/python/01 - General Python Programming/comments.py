# COMMENTS IN PYTHON

# Calculate the area of a circle given the radius
radius = 5
area = 3.1416 * radius ** 2  # Using π ≈ 3.1416 for calculation

# Define a threshold for classification decisions
threshold = 0.8

# Example of commented-out code (useful for debugging or reference)
# total = sum([1, 2, 3])
# print(total)
# print(max([5, 6, 1, -2]))

"""
Example of a multi-line comment (docstring style),
typically used for docstrings.

temp = preprocess_data(raw_input)
model.train(temp)
"""

# BEST PRACTICES FOR WRITING COMMENTS

# 1. Be Clear and Concise

counter = 0

# Bad comment: Too vague, doesn't add value
# increment
counter += 1

# Good comment: Clearly explains the purpose
# Increment the counter to track the number of iterations
counter += 1

# 2. Explain the "Why", Not Just the "What"

# Bad comment: States the obvious
# Set is_active to True
is_active = True

# Good comment: Provides context on why the value is set
# Activate the user account after email verification
is_active = True

# 3. Keep Comments Up-to-Date
# (Reminder: Ensure comments reflect the latest code logic)

# 4. Avoid Obvious Comments

# Bad comment: The code itself is self-explanatory
# Assign 5 to x
x = 5
