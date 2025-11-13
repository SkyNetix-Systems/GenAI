# COMMON STRING METHODS

# Demonstrating type checking for an integer and a string
x = 10
s = 'abc'
print(type(x), type(s))  # Output: <class 'int'> <class 'str'>

# STRING CASE CONVERSIONS

model_output = 'ai IS the future of everything!'

# Convert the string to uppercase
print(model_output.upper())  # 'AI IS THE FUTURE OF EVERYTHING!'

# Convert the string to lowercase
print(model_output.lower())  # 'ai is the future of everything!'

# The original string remains unchanged (strings are immutable)
print(model_output)  # 'ai IS the future of everything!'

# STRING STRIPPING

response = ' 🤖 Hello, human! 🤖 '

# Remove leading and trailing whitespace characters
print(response.strip())  # '🤖 Hello, human! 🤖'

# Remove specific leading and trailing characters (' 🤖')
print(response.strip(' 🤖'))  # 'Hello, human!'

# STRING REPLACEMENT

text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'

# Replace occurrences of 'ML' with 'machine learning'
updated_text = text.replace('ML', 'machine learning')
print(updated_text)
# 'machine learning is a critical component of modern AI. machine learning techniques are advancing rapidly.'

# STRING COUNTING

text = 'AI is the FUture. Embrace the future of AI!'

# Count occurrences of 'future' (case-insensitive)
print(text.lower().count('future'))  # Output: 2

# STRING SPLITTING

statement = 'AI breakthrough at every step'

# Split the string into a list of words
words = statement.split()
print(words)  # ['AI', 'breakthrough', 'at', 'every', 'step']

# STRING JOINING

terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']

# Join the list elements into a single string, separated by ', '
buzzwords_string = ', '.join(terms)
print(buzzwords_string)  # 'AI, ML, GenAI, LLM, NLP'

# STRING PREFIX AND SUFFIX REMOVAL (Python 3.9+)

url = 'https://example.com'

# Remove 'https://' from the beginning of the URL
cleaned_url = url.removeprefix('https://')
print(cleaned_url)  # 'example.com'

filename = 'state_of_ai_2025.pdf'

# Remove '.pdf' from the end of the filename
cleaned_filename = filename.removesuffix('.pdf')
print(cleaned_filename)  # 'state_of_ai_2025'

# USING HELP TO VIEW DOCUMENTATION

# Display available string methods and documentation
# help(str)

# Display help information for the `strip()` method
help(str.strip)
