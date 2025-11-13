# PYTHON STRING BASICS

# Defining string variables (use '' or "" but stay consistent)
model_summary = 'This AI model predicts stock trends.'
prediction_message = "AI will revolutionize industries!"

# Printing a basic string
print(model_summary)

# Example of using special characters in strings
feedback = 'Press the # button to continue.'

# Demonstrating escape characters for single quotes
print('AI says, I\'m here to assist you.')
print("AI says, I'm here to assist you.")

# Using a multi-line string
ai_response = '''Hello there!
I’m an AI here to help.
Feel free to ask me anything.
'''
print(ai_response)

# Using `\n` for multi-line text representation
ai_prompt = 'Welcome to AI Bot\nYour virtual assistant\nHere to assist with all things tech!'
print(ai_prompt)

# Demonstrating the use of escape character `\`
print('\\ is essential for handling escape characters in Python.')

# Using a backslash `\` to split a long string across multiple lines
gen_ai_message = 'Generative AI has revolutionized the way we create, ' \
                 'from text generation to image synthesis. It is like having a creative partner!'
print(gen_ai_message)

# Printing non-English text
print('こんにちはPython！')  # This says 'Hello Python!' in Japanese

# Printing an emoji for fun. Python strings are UTF-8 encoded.
print('🤖')
