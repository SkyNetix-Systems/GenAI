# CONDITIONAL STATEMENTS (if ... elif ... else)

# Syntax reminder:
# if some_condition_is_true:
#     # Code block 1 (executes if the condition is met)
# elif some_other_condition_is_true:
#     # Code block 2 (executes if the first condition is false but this one is met)
# else:
#     # Code block 3 (executes if none of the above conditions are met)

# Prompt the user to enter the temperature in Celsius
temperature = int(input('Enter the temperature in Celsius: '))

# Check the temperature range and provide appropriate clothing advice
if temperature < 0:
    print("It's freezing, wear a heavy coat!")
elif temperature < 15:
    print("It's chilly! You might need a jacket!")
elif temperature < 27:
    print("The weather is mild. A light sweater should be enough.")
else:
    print("It's hot! Stay cool and hydrated.")

# CONDITIONAL STATEMENTS WITH A STATIC VALUE

# Example where the temperature value is predefined
temperature = 10  # This value could satisfy multiple conditions

# The first matching condition executes, and the remaining conditions are skipped
if temperature < 15:  # This condition is True
    print("It's chilly! You might need a jacket.")
elif temperature < 27:  # This condition is also True, but it will be skipped
    print("The weather is mild. A light sweater should be enough.")
else:
    print("It's hot! Stay cool and hydrated.")

# Note: The first condition that evaluates to True stops further checks
