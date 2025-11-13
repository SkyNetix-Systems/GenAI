# Tuple operations

# Concatenating tuples
coordinates = (37.7749, -122.4194)
meta_data = ('Latitude', 'Longitude')
full_data = coordinates + meta_data  # Combine tuples
print(full_data)  # Output: (37.7749, -122.4194, 'Latitude', 'Longitude')

# Repeating tuples
repeated_tuple = (1, 2) * 3  # Repeat the tuple 3 times
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# Slicing tuples (creates a new tuple with the specified elements)
tuple_data = (1, 2, 3, 4, 5)
sliced = tuple_data[1:3]  # Elements from index 1 up to (but not including) index 3
print(sliced)  # Output: (2, 3)

reversed_data = tuple_data[::-1]  # Reverse the tuple using slicing
print(reversed_data)  # Output: (5, 4, 3, 2, 1)

# Counting elements (count())
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))  # Count the number of occurrences of 2 (Output: 3)

# Iteration
for label in meta_data:
    print(f'Data label: {label}')

# Sorting (sorted() returns a new sorted list, tuples are immutable)
t1 = (4, 3, 10)
print(sorted(t1))  # Output: [3, 4, 10] (returns a list)
print(t1) # (4,3,10) - original tuple is unchanged