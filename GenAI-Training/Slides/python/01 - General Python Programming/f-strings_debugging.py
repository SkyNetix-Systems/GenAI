name, age = 'Alice', 30
print(f'Your name is {name} and you are {age} old.')

# Debugging with variable names included in output
print(f'Your name is {name=} and you are {age=} old.')

# Example with an expression
r = 13.3
PI = 3.141592
print(f'Circle area with a radius of {r} is {PI * r**2}')

# Debugging with expressions
print(f'Circle area with a radius of {r=} is {PI * r**2=}')

# Formatting output with 3 decimal places
print(f'Circle area with a radius of {r=} is {PI * r**2=:.3f}')
