# GETTING USER INPUT

# BASIC USER INPUT

# Prompt the user to ask a question
# command = input('Ask your AI assistant a question: ')
# print('Your question was:', command)

# USER INPUT RETURNS A STRING

training_hours = input('Enter hours spent training the model: ')

# Demonstrate that `input()` always returns a string
print('Data type of training_hours:', type(training_hours))  # Output: <class 'str'>

# CONVERTING USER INPUT TO NUMERIC TYPES

iterations = int(input('Enter the number of model iterations: '))
datasets = int(input('Enter the number of datasets: '))

total = iterations * datasets
print('Total processing units:', total)
