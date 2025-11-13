# Working with Ranges in Python

# -----------------------------
# 1. Using range() in a Loop
# -----------------------------

# Assigning unique IDs to participants from 1 to 100
for participant_id in range(1, 101):  # range(start, stop) -> stop is exclusive
    print(f'Assigning ID to participant #{participant_id}')

# -----------------------------
# 2. Creating a List from a Range
# -----------------------------

# Generate a list of even numbers from 0 to 8
numbers = list(range(0, 10, 2))  # range(start, stop, step)
print(numbers)  # Output: [0, 2, 4, 6, 8]

# -----------------------------
# 3. Looping a Fixed Number of Times (Ignoring Index)
# -----------------------------

# Loop 5 times without using the index variable
for _ in range(5):  # The underscore (_) is a convention for an unused variable
    print('Analyzing Data')
