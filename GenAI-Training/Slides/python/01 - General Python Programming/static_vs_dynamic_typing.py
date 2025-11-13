# Static vs. Dynamic Typing

# Java (example - for comparison)
# int score;  // Declaration: score is of type integer
# score = 10; // Assignment: value 10 is assigned to score

# Python (dynamic typing)
score = 10          # score is dynamically assigned the type int
print(type(score))  # Output: <class 'int'>

score = 'Python'    # score is now dynamically reassigned to the type str
print(type(score))  # Output: <class 'str'>

# Key difference:
# - Java, C++, Go: Static typing.  Variable type is declared and fixed.  Compiler checks type compatibility.
# - Python: Dynamic typing. Variable type is inferred at runtime based on the assigned value.  Type can change.