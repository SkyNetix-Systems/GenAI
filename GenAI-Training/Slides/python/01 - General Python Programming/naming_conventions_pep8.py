# Naming Conventions in Python (PEP 8)

# -----------------------------
# 1. Allowed Characters (a-z, A-Z, 0-9, and _)
# -----------------------------

total_count = 100   # ✅ Valid: Uses letters and underscore
_hidden_value = 42  # ✅ Valid: Leading underscore implies a "private" variable (not enforced)
# 1st_place = 'Gold'  # ❌ Invalid: Cannot start with a digit

# -----------------------------
# 2. Avoid Leading Underscores (Except for Private/Internal Use in Classes)
# -----------------------------

# _variable: Often used as a convention to indicate "internal use" (not enforced)

# -----------------------------
# 3. No Special Characters or Spaces (!, %, @, ?, ., etc.)
# -----------------------------

# user-name = 'Alice'  # ❌ Invalid: Hyphens are not allowed
# user name = 'Bob'    # ❌ Invalid: Spaces are not allowed

# -----------------------------
# 4. Reserved Words (if, else, while, for, etc.)
# -----------------------------

# if = 10  # ❌ Invalid: Cannot use Python keywords as variable names

# -----------------------------
# 5. Case Sensitivity
# -----------------------------

# Python is case-sensitive, so `Max_Value` and `max_value` are different variables.

# -----------------------------
# 6. Use Descriptive Names and snake_case (Recommended)
# -----------------------------

max_value = 99       # ✅ Descriptive and uses snake_case
total_items = 15     # ✅ Clear and follows PEP 8
# maxValue = 'this is camelCase'  # ❌ Not recommended in Python (CamelCase is for class names)

# -----------------------------
# 7. Don't Shadow Built-in Names
# -----------------------------

list = [1, 2, 3]  # ❌ Not recommended: Shadows the built-in list() function

# -----------------------------
# 8. Constants (Use ALL_CAPS)
# -----------------------------

PI = 3.1416
DAYS_IN_YEAR = 365
MAX_CONNECTIONS = 10  # ✅ Constants should be in uppercase with underscores
