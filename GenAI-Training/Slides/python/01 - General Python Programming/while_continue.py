# Smart looping techniques: continue, pass, break

sentence = 'AI is the future of technology.'
for word in sentence.split():
    if word in ['the', 'in', 'of']:
        continue  # Skip the current iteration and move to the next one
    print(word, end=' ')  # Output: AI is future technology.

print()  # Add a newline for better formatting

while True:
    prompt = input('Enter a prompt for the model: ')
    if len(prompt) < 5:
        print('Prompt too short. Try again!')
        continue  # Go back to the beginning of the loop
    print(f'Processing your prompt: {prompt}')
    break  # Exit the loop if the prompt is long enough

# pass - A null operation.
# It is used when a statement is required syntactically, but you do not want to execute any commands or code.
# It's often used as a placeholder.

for model in range(5):
    pass  # Placeholder while you finalize the setup or logic for each model
    # Add the actual code for processing each model here later.