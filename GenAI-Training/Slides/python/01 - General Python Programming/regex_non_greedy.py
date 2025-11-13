# Regular Expressions - Non-Greedy Matching

import re  # Importing the regex module

# Sample HTML string
html = '<div><p>Welcome to AI</p></div>'

# Non-greedy match: Matches the first occurrence of a tag using `*?`
match = re.search(r'<.*?>', html)

# Display the first matched tag
if match:
    print(match.group())  # Output: <div>
