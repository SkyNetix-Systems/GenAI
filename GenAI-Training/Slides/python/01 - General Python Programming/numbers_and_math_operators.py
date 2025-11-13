# Numbers and Math Operators in Python

# -----------------------------
# 1. Basic Arithmetic Operators
# -----------------------------

# Addition (+) and Subtraction (-)
print(8 + 3)   # Output: 11
print(10 - 4)  # Output: 6

# Multiplication (*)
print(5 * 2)   # Output: 10

# Division (/): Always returns a float
print(8 / 2)   # Output: 4.0

# -----------------------------
# 2. Advanced Math Operators
# -----------------------------

# Floor Division (//): Rounds down to the nearest whole number
print(11 // 5)  # Output: 2

# Multiplication with float values
print(5 * 2.0)  # Output: 10.0 (float result)

# Exponentiation (**): Raises a number to a power
print(2 ** 3)  # Output: 8 (2^3)

# Modulus (%): Returns the remainder of a division
print(8 % 5)  # Output: 3 (8 divided by 5 gives remainder 3)

# -----------------------------
# 3. Operator Precedence
# -----------------------------

# Parentheses control order of operations, exponentiation has higher precedence
print((2 + 4) * 2 ** 3)  # Output: 48
# Equivalent to: (6) * (8) -> 48

# -----------------------------
# 4. Large Numbers Formatting
# -----------------------------

# Using underscores (_) for better readability (Python ignores them)
print(1_000_000_003_004)  # Output: 1000000003004
