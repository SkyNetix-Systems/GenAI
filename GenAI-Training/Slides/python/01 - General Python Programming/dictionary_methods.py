# DICTIONARY OPERATIONS AND METHODS: ACCESSING, UPDATING, .GET(), .KEYS(), AND .VALUES()

# ASSIGNMENT AND COPYING

# Creating a dictionary
model_params = {'layers': 24, 'units': 512, 'activation': 'relu'}

# Assigning the same dictionary reference to another variable (not a copy)
shared_params = model_params  # Both variables point to the same dictionary

# Modifying the dictionary affects both variables
model_params['activation'] = 'gelu'
print(shared_params)
# Output: {'layers': 24, 'units': 512, 'activation': 'gelu'}

# Creating a separate copy of the dictionary to avoid unintentional modifications
safe_params = model_params.copy()

# Modifying model_params does not affect safe_params (since it's a separate copy)
model_params['layers'] = 48
print(safe_params)
# Output: {'layers': 24, 'units': 512, 'activation': 'gelu'}

# MERGING DICTIONARIES WITH update()

base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rate': 0.001, 'units': 128}

# Merge version_config into base_config (overwriting matching keys)
base_config.update(version_config)
print(base_config)
# Output: {'batch_size': 32, 'epochs': 10, 'learning_rate': 0.001, 'units': 128}

# CLEARING A DICTIONARY

# Removes all key-value pairs from model_params
model_params.clear()
print(model_params)  # Output: {}

# DICTIONARY VIEWS WITH .keys(), .values(), AND .items()

# Get all keys from base_config
print(base_config.keys())
# Output: dict_keys(['batch_size', 'epochs', 'learning_rate', 'units'])

# Get all values from base_config
print(base_config.values())
# Output: dict_values([32, 10, 0.001, 128])

# Iterate through key-value pairs
for key, value in base_config.items():
    print(f'{key} => {value}')
# Output:
# batch_size => 32
# epochs => 10
# learning_rate => 0.001
# units => 128

# TESTING MEMBERSHIP USING in

# Check if a key exists in the dictionary
print('batch_size' in base_config)  # Output: True

# Check if a value exists in the dictionary
print(32 in base_config.values())  # Output: True

# Check if a key-value pair exists in the dictionary
print(('batch_size', 32) in base_config.items())  # Output: True

# SET OPERATIONS WITH DICTIONARY KEYS AND ITEMS

config_a = {'batch_size': 32, 'optimizer': 'adam'}
config_b = {'batch_size': 64, 'optimizer': 'adam', 'momentum': 0.9}

# Find common keys between two dictionaries using set intersection
common_keys = config_a.keys() & config_b.keys()
print(common_keys)
# Output: {'batch_size', 'optimizer'}

# ITERATING OVER KEYS, VALUES, AND ITEMS

# Iterate over keys
for key in base_config:
    print(f'Key: {key}')

# Iterate over values
for value in base_config.values():
    print(f'Value: {value}')

# Iterate over key-value pairs
for key, value in base_config.items():
    print(f'{key} => {value}')
