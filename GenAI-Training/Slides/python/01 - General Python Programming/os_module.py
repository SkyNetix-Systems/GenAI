# Working with the OS Module in Python

import os  # Importing the OS module for file and directory operations

# -----------------------------
# 1. Creating a Directory (if it doesn't exist)
# -----------------------------

output_dir = 'processed_embeddings'

# Check if the directory exists before creating it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Creates the directory
    print(f'Directory "{output_dir}" created.')
else:
    print(f'Directory "{output_dir}" already exists.')

# -----------------------------
# 2. Checking if a File Exists
# -----------------------------

model_path = 'config.json'

# Check if the specified file exists
if os.path.isfile(model_path):
    print(f'File "{model_path}" exists.')
else:
    print(f'File "{model_path}" does not exist.')

# -----------------------------
# 3. Listing Directory Contents
# -----------------------------

# List contents of the current working directory
print('Current directory contents:', os.listdir())

# List contents of a specific directory (Windows example)
target_dir = r'C:\Go'  # Use raw string (r'path') to avoid escape sequences
if os.path.exists(target_dir):
    print(f'Contents of "{target_dir}":', os.listdir(target_dir))
else:
    print(f'Directory "{target_dir}" does not exist.')

# -----------------------------
# 4. Getting the Current Working Directory (CWD)
# -----------------------------

current_directory = os.getcwd()  # Get the current working directory
print('Current working directory:', current_directory)

# -----------------------------
# 5. Changing the Current Directory
# -----------------------------

os.chdir('..')  # Moves one level up in the directory structure
print('Directory changed to:', os.getcwd())
