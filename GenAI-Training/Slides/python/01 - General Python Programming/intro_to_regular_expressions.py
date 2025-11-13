# INTRODUCTION TO REGULAR EXPRESSIONS (REGEX)

import re  # Importing the regex module

# Basic regex patterns:
# - \d  : Matches any digit (0-9)
# - \w  : Matches any alphanumeric character, including underscore (a-z, A-Z, 0-9, _)
# - \s  : Matches any whitespace character (space, tab, newline)
# - .   : Matches any character except a newline

# Quantifiers:
# - +   : Matches one or more occurrences
# - *   : Matches zero or more occurrences
# - ?   : Matches zero or one occurrence
# - {n} : Matches exactly n occurrences
# - {n,m}: Matches between n and m occurrences

# Example: Extracting hashtags from a post
# post = 'Exploring the future with #ArtificialIntelligence and #MachineLearning! #AI #GenAI'
# hashtags = re.findall(r'#\w+', post)  # Finds words that start with '#'
# print(hashtags)  # Output: ['#ArtificialIntelligence', '#MachineLearning', '#AI', '#GenAI']

# Using Anchors and Grouping for Precise Matching:
# - ^  : Matches the start of a string
# - $  : Matches the end of a string

command = '/execute data-analysis'  # Example command
if re.match(r'^/execute\s\w+(-\w+)*$', command):
    # Matches a command starting with '/execute', followed by a word or hyphenated words
    print('Valid command')
else:
    print('Invalid command')

# Extracting user mentions from a message
message = 'Great job @alice and @bob on the AI model!'
mentions = re.findall(r'@(\w+)', message)  # Captures words prefixed with '@'
print('Notify users:', mentions)  # Output: ['alice', 'bob']
