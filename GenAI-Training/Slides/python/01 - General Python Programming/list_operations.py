# List Operations: Concatenation, Slicing, and Iteration

# -----------------------------
# 1. List Concatenation
# -----------------------------

l1 = [3, 4]
print(l1, id(l1))   # Prints list and its memory address

l1 = l1 + [5, 6]    # Creates a new list (concatenation)
print(l1, id(l1))   # Memory address changes

l1 += [7, 8]        # Modifies the existing list in place
print(l1, id(l1))   # Memory address remains the same

# extend() adds elements individually
l1.extend([11, 12])
print(l1)  # Output: [3, 4, 5, 6, 7, 8, 11, 12]

# append() vs extend()
l1.append(['a', 'b'])   # Appends the list as a single element
l1.extend(['x', 'y'])   # Extends the list with individual elements
print(l1)               # Output: [3, 4, 5, 6, 7, 8, 11, 12, ['a', 'b'], 'x', 'y']

# -----------------------------
# 2. List Slicing
# -----------------------------

numbers = [1, 2, 3, 4, 5]

# Slicing [start:end] (end is exclusive)
nums = numbers[1:4]
print(f'nums: {nums}')          # Output: [2, 3, 4]
print(f'numbers: {numbers}')    # Original list remains unchanged

# Various slicing examples
print(numbers[:3])    # Output: [1, 2, 3] (first three elements)
print(numbers[2:])    # Output: [3, 4, 5] (from index 2 onward)
print(numbers[1:5:2]) # Output: [2, 4] (step of 2)
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1] (reversed list)

# -----------------------------
# 3. Iteration and Membership Testing
# -----------------------------

ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']

# Iterating over the list
for ip in ip_list:
    print(f'Connecting to {ip} ...')

# Checking for membership in a list
target_ip = '10.0.0.1'
if target_ip in ip_list:
    print(f'{target_ip} is in the list')

prefix = '192'
if prefix not in ip_list:
    print(f'No addresses with the prefix {prefix} found in the list')

# -----------------------------
# LIST GOTCHAS (Common Pitfalls)
# -----------------------------

# 1. Modifying one list affects another if they share the same reference
l1 = [1, 2, 3]
l2 = l1  # l2 references the same object as l1
l2[0] = 'xx'
l2.append(10)
print(l2, l1)  # Both lists are modified because they reference the same object

# To avoid this, use list.copy() for a shallow copy
l3 = l1.copy()
l3.append('abc')
print(l3, l1)  # l3 is modified independently

# 2. Removing items from a list while iterating can cause unexpected behavior
nums = [1, 2, 3, 4, 5, 6, 7]
for n in nums:
    if n < 5:
        nums.remove(n)  # This skips elements because the list shrinks while iterating
print(nums)             # Output may be unexpected: [2, 4, 5, 6, 7]

# Correct approach: Create a new list instead of modifying the original one during iteration
new_list = [n for n in nums if n >= 5]
print(new_list)  # Output: [5, 6, 7]
