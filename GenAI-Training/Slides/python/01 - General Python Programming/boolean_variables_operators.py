# BOOLEAN VARIABLES AND LOGICAL OPERATORS

# Boolean variables representing workout completion status
cardio_completed = True
strength_completed = False

# Bonus points are calculated by adding boolean values
# (True is treated as 1, and False as 0)
bonus_points = cardio_completed + strength_completed

# Check if the user has earned any bonus points
if bonus_points > 0:
    print(f'Great job! You’ve earned {bonus_points} bonus point(s) for today’s workout!')
else:
    print('No bonus points today. Try completing a session to earn points!')

# STRING TRUTHINESS CHECK

# Define a username
username = 'john'

# Check if the username is not an empty string (non-empty strings evaluate to True)
if username:
    print(f'Welcome back, {username}!')
else:
    print('Please enter your username.')
