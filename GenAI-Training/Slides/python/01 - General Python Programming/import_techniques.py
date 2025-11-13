# ADVANCED IMPORT TECHNIQUES

# Standard import: Importing the entire module
# import random
# print(random.randint(1, 100))
# print(random.choice(['apple', 'banana', 'cherry']))

# Selective import: Importing specific functions from the module
# from random import randint, choice
# print(randint(1, 100))
# print(choice(['apple', 'banana', 'cherry']))

# Alias import: Importing the module with an alias
# import random as rnd
# print(rnd.randint(1, 100))
# print(rnd.choice(['apple', 'banana', 'cherry']))

# Wildcard import (not recommended)
from random import *
print(randint(1, 100))
print(choice(['apple', 'banana', 'cherry']))