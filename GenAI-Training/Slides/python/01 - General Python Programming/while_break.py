# THE break STATEMENT

# Using break in a for loop
keywords = ['innovation', 'deep learning', 'AI revolution', 'neural networks', 'machine learning']

for word in keywords:
    print(f'Checking word: {word}')
    if word == 'AI revolution':
        print('Urgent keyword found! Stopping search.')
        break  # Exits the loop as soon as 'AI revolution' is found

# Example of using break in a while loop with user input
# while True:
#     user_input = input('Say the magic word to start: ')
#     if user_input.lower() == 'launch':
#         print('🚀 Starting the AI-powered chatbot!')
#         break  # Exits the loop once the correct word is entered
#     print('Hmm, that’s not the magic word. Try again!')

# Using break in a while loop
temperature = 70

while temperature < 80:
    print(f'The current temperature is {temperature}°F.')

    if temperature == 75:
        print('Temperature threshold reached. Stopping monitoring.')
        break  # Exits the loop once temperature reaches 75

    temperature += 1
else:
    print('Temperature monitoring complete. System stable.')  # This won't execute if break is triggered

# Using break in a nested loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Exits the inner loop when j equals 1
    print(f'i={i}, j={j}')  # j retains its last value before break
