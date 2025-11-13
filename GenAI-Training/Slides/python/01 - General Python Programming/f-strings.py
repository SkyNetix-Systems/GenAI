# FORMATTED STRINGS: USING F-STRINGS FOR CLEAN OUTPUT

# STRING CONCATENATION (LESS EFFICIENT)
model_name = 'GPT'
version = 4

# Traditional concatenation (requires explicit type conversion)
print('Hello from ' + model_name + '-' + str(version) + '!')

# USING F-STRINGS (MORE READABLE & EFFICIENT)

# The f-string automatically converts variables to strings
print(f'Hello from {model_name}-{version}!')
# Output: Hello from GPT-4!

# FORMATTING NUMBERS WITH F-STRINGS

token_used = 123
cost_per_token = 0.001

# Formatting a floating-point number to 4 decimal places
total_cost = f'{token_used * cost_per_token}'
print(f'Total cost for this message: {total_cost}')
# Output: Total cost for this message: 0.1230

# INLINE VARIABLE DISPLAY USING F-STRINGS (Python 3.8+)

learning_rate, epochs = 0.01, 10

# The `=` syntax displays both the variable name and its value
print(f'Learning rate: {learning_rate=}, Epochs: {epochs=}')
# Output: Learning rate: learning_rate=0.01, Epochs=10

# CALCULATING AND FORMATTING PRECISION

true_positive = 42
false_positive = 8

# Compute precision and format it to 3 decimal places
precision = true_positive / (true_positive + false_positive)
print(f'Precision: {precision=:.3f}')
# Output: Precision: precision=0.840