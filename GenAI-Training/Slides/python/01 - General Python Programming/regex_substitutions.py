# Regular Expressions - Substitutions using re.sub()

import re  # Importing the regex module

# -----------------------------
# 1. Anonymizing Email Addresses
# -----------------------------

log = "User john.doe@ai-company.com accessed the system."

# Regex to match email addresses: [username]@[domain]
# \w  -> Matches letters, digits, or underscores
# \.- -> Matches dots and hyphens (in domain and username)
anonymized_log = re.sub(r'[\w\.-]+@[\w\.-]+', '[***]', log)

print(anonymized_log)
# Output: "User [***] accessed the system."

# -----------------------------
# 2. Date Format Conversion (DD/MM/YYYY → YYYY-MM-DD)
# -----------------------------

text = "The AI conference is scheduled for 15/08/2025."

# Capturing groups: (\d{2})/(d{2})/(\d{4}) -> Matches date components
# Replacement order: \3-\2-\1 -> Rearranges as YYYY-MM-DD
standardized_text = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text)

print(standardized_text)
# Output: "The AI conference is scheduled for 2025-08-15."
