# DICTIONARY BASICS

# Creating a dictionary with various key types
model_config = {
    'model_name': 'GPT-4',   # String key
    'layers': 48,            # Integer key
    'parameters': '175B',    # String key
    (1, 2): 10               # Tuple key (immutable, valid for dictionary keys)
}

# Check the type of model_config
print(type(model_config))  # Output: <class 'dict'>

# DEFINING A DICTIONARY

# Dictionary storing hyperparameter settings
hyperparameters = {
    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': 'Adam'
}

# ADDING A NEW KEY-VALUE PAIR

# Adding batch_size to hyperparameters
hyperparameters['batch_size'] = 64
print(hyperparameters)
# {'learning_rate': 0.0001, 'dropout_rate': 0.3, 'optimizer': 'Adam', 'batch_size': 64}

# ACCESSING DICTIONARY VALUES

# Accessing a value using a key
print(hyperparameters['learning_rate'])  # Output: 0.0001

# SAFE KEY ACCESS USING .get()

# Using .get() to access a key that may not exist
# This avoids KeyError and provides a default value if the key is missing
print(hyperparameters.get('momentum', 'Not specified'))  # Output: 'Not specified'

# BEST PRACTICES FOR DICTIONARIES

# 1. Stick to **immutable keys** (e.g., strings, numbers, tuples)
# 2. Avoid **duplicate keys** (last assigned value will override)
# 3. Use **.get()** for safe access to prevent errors

# NESTED DICTIONARIES

# A dictionary storing configuration settings for different models
pipeline_config = {
    'GPT-4': {'layers': 48, 'parameters': '175B', 'attention_heads': 96},
    'BERT': {'layers': 24, 'parameters': '345M', 'attention_heads': 16}
}

# Accessing a nested value (number of attention heads in GPT-4)
print(pipeline_config['GPT-4']['attention_heads'])  # Output: 96
