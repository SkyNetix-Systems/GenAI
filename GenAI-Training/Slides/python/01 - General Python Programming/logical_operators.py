# Logical Operators in Python: and, or, not

# -----------------------------
# 1. Using 'and' Operator
# -----------------------------

age = 27
has_student_id = True

# 'and' requires both conditions to be True
if age < 18 and has_student_id:
    print('You are eligible for the student discount!')
else:
    print('Sorry, you don\'t qualify for the student discount!')

# -----------------------------
# 2. Using 'or' Operator
# -----------------------------

first_time_user = False
has_promo_code = True

# 'or' requires at least one condition to be True
if first_time_user or has_promo_code:
    print('Discount applied!')
else:
    print('No discount available.')

# -----------------------------
# 3. Using 'not' Operator
# -----------------------------

profile_completed = False

# 'not' negates the boolean value
if not profile_completed:
    print('Please complete your profile to access all features.')
else:
    print('Your profile is complete!')

# -----------------------------
# 4. Combining Logical Operators
# -----------------------------

age = 16
has_parental_consent = True

# The 'not' operator negates the entire condition
if not (age >= 18 or has_parental_consent):
    print('You cannot sign up without parental consent.')
else:
    print('You are allowed to sign up.')

# -----------------------------
# 5. Short-Circuit Evaluation
# -----------------------------

temperature = 15
is_sunny = False

# Short-circuiting: If temperature > 25 is False, Python skips checking is_sunny
if temperature > 25 and is_sunny:
    print('Perfect day for the beach!')
else:
    print('Maybe another day for the beach!')

# -----------------------------
# 6. Logical Operators with Strings
# -----------------------------

email = 'user@example.com'
phone_number = ''

# Since non-empty strings evaluate to True, 'or' selects the first True value
if email or phone_number:
    print('Thank you for providing your contact information!')
else:
    print('Please provide either a phone number or an email address to continue.')
