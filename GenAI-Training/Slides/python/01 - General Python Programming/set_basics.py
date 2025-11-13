# Sets basics

# Create a set of unique elements (unordered and no duplicates)
unique_ids = {1, 2, 3, 'a', 'b', 4}
# print(unique_ids[0])  # Error: Sets do not support indexing

# Print the set (order is not guaranteed)
print(unique_ids)

# Create an empty set ({} creates an empty dictionary, not a set)
empty_set = set()

# Check the type of {} (it's a dictionary)
print(type({}))  # Empty dict, not set

# Create a set from a list to get unique sentences
sentences = ['Hello world', 'AI is amazing', 'Hello world', 'Python is great']
unique_sentences = set(sentences)  # Duplicate 'Hello world' is removed
print(unique_sentences)

# Create an immutable set (frozenset)
immutable_tokens = frozenset(unique_ids)
print(immutable_tokens)

# immutable_tokens.add('abc') # Error: Cannot add to a frozenset (it's immutable)