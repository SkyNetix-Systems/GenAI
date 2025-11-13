# Essential Regex Techniques for Text Processing

import re  # Importing the regex module

# -----------------------------
# 1. Extracting IP Addresses from Log Files
# -----------------------------

# Read the contents of a log file
with open('access_logs.txt') as f:
    logs = f.read()

# Regex pattern to match IPv4 addresses
ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', logs)
print(ip_addresses)  # Output: List of extracted IP addresses

# -----------------------------
# 2. Splitting Text into Sentences
# -----------------------------

text = 'Welcome to AI. Let’s explore the future! Are you ready?'

# Split text using regex on sentence-ending punctuation (.!?), followed by a space
sentences = re.split(r'[.!?]\s', text)
print(sentences)  # Output: ['Welcome to AI', 'Let’s explore the future', 'Are you ready?']

# -----------------------------
# 3. Extracting Error Messages from Logs
# -----------------------------

logs = """INFO: Starting server...
ERROR: Failed to connect to database
INFO: Retrying connection...
ERROR: Connection timeout
INFO: Server stopped."""

# Extract messages following "ERROR:"
errors = re.findall(r'ERROR: (.+)', logs, re.MULTILINE)
print(errors)  # Output: ['Failed to connect to database', 'Connection timeout']

# -----------------------------
# 4. Using re.compile() for Pattern Reuse
# -----------------------------

# Compile a regex pattern for exact word match ('AI')
pattern = re.compile(r'\bAI\b')

# List of sample texts
texts = ['AI is transforming industries.', 'Welcome to AI.']

# Find occurrences of 'AI' in each text
for text in texts:
    print(pattern.findall(text))  # Output: ['AI'] if found, otherwise []

