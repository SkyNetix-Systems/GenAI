# LIST COMPREHENSIONS

# Doubling values using a traditional for loop
clicks = [10, 5, 15, 20]
doubled_clicks = []

for c in clicks:
    doubled_clicks.append(c * 2)

print(doubled_clicks)  # Output: [20, 10, 30, 40]

# List comprehension syntax: [expression for item in iterable]
doubled_clicks = [c * 2 for c in clicks]
print(doubled_clicks)  # Output: [20, 10, 30, 40]

# Formatting names with list comprehension
contributors = ['alice', 'Bob', 'CHARLIE']
formatted_names = [name.capitalize() for name in contributors]
print(formatted_names)  # Output: ['Alice', 'Bob', 'Charlie']

# List comprehension with a condition: [expression for item in iterable if condition]
nums = [1, 7, 8, 14, 21, 30, 50]
divisible_by_seven = [n for n in nums if n % 7 == 0]
print(divisible_by_seven)  # Output: [7, 14, 21]

# Finding shared skills between two teams
ai_team = ['Alice', 'Bob', 'Charlie']
data_team = ['Alice', 'David', 'Charlie']
shared_skills = [name for name in ai_team if name in data_team]
print(shared_skills)  # Output: ['Alice', 'Charlie']
