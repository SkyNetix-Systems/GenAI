# FOR LOOPS

# Types of loops:
# 1. For loops - iterate over sequences (lists, tuples, strings, dictionaries, etc.)
# 2. While loops - execute as long as a condition is True

# ITERATING OVER A LIST OF NUMBERS

numbers = [1, 2, 3, 4, 5]

# Loop through each number in the list
for number in numbers:
    print(number)
# Output: 1 2 3 4 5 (printed on separate lines)

# FILTERING TWEETS CONTAINING AI OR MACHINE LEARNING

tweets = [
    'Exploring AI applications',
    'Machine Learning is the future',
    'Having lunch with friends',
    'New advances in GenAI'
]

# Loop through each tweet and filter those related to AI or Machine Learning
for tweet in tweets:
    if 'AI' in tweet or 'Machine Learning' in tweet:
        print(f'Filtered tweet: {tweet}')

# CASE-INSENSITIVE STRING MATCHING (FILTERING FEEDBACK)

feedback = [
    'Great service!',
    'Excellent response time',
    'Had to wait too long',
    'Excellent support from staff'
]

# Highlight feedback that contains the word "excellent" (case-insensitive)
for comment in feedback:
    if 'excellent' in comment.lower():  # Convert to lowercase for case-insensitive search
        print(f'Highlighted Feedback: {comment}')


temperature_readings = [71, 74, 78, 82, 85, 90]  # Sample data in Fahrenheit
threshold = 80  # Safe temperature threshold

# Check if any temperature exceeds the threshold
for temp in temperature_readings:
    if temp > threshold:
        print(f'Warning: Temperature exceeded safe limit at {temp}°F')
        