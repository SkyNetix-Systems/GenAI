import sys
import os

# Get the filename to rename from the user
old_file_name = input('Enter the filename to rename: ')

# Check if the file exists
if not os.path.isfile(old_file_name):
    print(f'File {old_file_name} does not exist!')
    sys.exit()  # Exit the program if the file doesn't exist

# Get the new filename from the user
new_file_name = input('Enter the new filename: ')

# Rename the file
os.rename(old_file_name, new_file_name)
print(f'File renamed from {old_file_name} to {new_file_name}')

# os.remove() -  Deletes a file
# os.rmdir() - Deletes a directory (must be empty)