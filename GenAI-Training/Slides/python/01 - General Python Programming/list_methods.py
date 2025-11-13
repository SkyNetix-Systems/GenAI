# ESSENTIAL LIST METHODS IN PYTHON

l1 = list()
print(dir(l1))  # Displays a list of available methods for the list object

# -----------------------------
# ADDING ELEMENTS TO A LIST
# -----------------------------

# append(): Adds a single element to the end of the list
list1 = [1, 2.2, 'abc']
list1.append([5, 7])  # Appends a list as a single element
print(list1)  # Output: [1, 2.2, 'abc', [5, 7]]

# extend(): Extends the list with elements from an iterable
list1.extend(['x', 'y'])  # Adds each element separately
print(list1)  # Output: [1, 2.2, 'abc', [5, 7], 'x', 'y']

# insert(): Inserts an element at a specific index
years = [2021, 2022, 2024]
years.insert(2, 2023)  # Inserts 2023 at index 2
print(years)  # Output: [2021, 2022, 2023, 2024]

# -----------------------------
# REMOVING ELEMENTS FROM A LIST
# -----------------------------

# clear(): Removes all elements from the list
l1 = ['a', 'b', 'c']
l1.clear()
print(l1)  # Output: []

# pop(): Removes and returns an element by index (default is the last element)
l2 = [10, 20, 30, 40]
x = l2.pop()  # Removes the last element
print(x, l2)  # Output: 40 [10, 20, 30]

y = l2.pop(1)  # Removes the element at index 1
print(y, l2)  # Output: 20 [10, 30]

# remove(): Removes the first occurrence of a specified value
l3 = [10, 20, 10, 40]
l3.remove(10)  # Removes the first occurrence of 10
print(l3)  # Output: [20, 10, 40]

# Removing all occurrences of a specific value
l4 = [10, 20, 10, 40]
while 10 in l4:
    l4.remove(10)
print(l4)  # Output: [20, 40]

# -----------------------------
# COUNTING ELEMENTS IN A LIST
# -----------------------------

# count(): Counts occurrences of a specific element
letters = list('abaca')  # Converts a string into a list of characters
print(letters)              # Output: ['a', 'b', 'a', 'c', 'a']
print(letters.count('a'))   # Output: 3

# -----------------------------
# REVERSING AND SORTING LISTS
# -----------------------------

# reverse(): Reverses the order of elements in place
sequence = [1, 2, 3, 4]
sequence.reverse()
print(sequence)  # Output: [4, 3, 2, 1]

# sort(): Sorts the list in ascending order (default), or descending if reverse=True
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)      # Sorts in descending order
print(numbers)                  # Output: [5, 4, 3, 1, 1]

# sorted(): Returns a new sorted list without modifying the original
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers, reverse=True)  # Creates a new sorted list
print(numbers, sorted_numbers)                  # Output: [3, 1, 4, 1, 5] [5, 4, 3, 1, 1]
