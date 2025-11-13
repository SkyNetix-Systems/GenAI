# SET AND DICTIONARY COMPREHENSIONS

# SET COMPREHENSIONS

names = {'alice', 'BOB', 'charlie', 'DAVE'}

# Convert all names to capitalize first letter, ensuring consistent formatting
formatted_names = {name.capitalize() for name in names}

print(formatted_names)
# Output: {'Alice', 'Bob', 'Charlie', 'Dave'} (order may vary due to set nature)

# DICTIONARY COMPREHENSIONS

# Original dictionary
hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}

# Create a new dictionary where all values are doubled
adjusted_params = {k: v * 2 for k, v in hyperparams.items()}
print(adjusted_params)
# {'layers': 6, 'units': 512, 'dropout': 0.4}

# Create a set of keys (in uppercase) where values are greater than 0.2
updated_params = {k.upper() for k, v in hyperparams.items() if v > 0.2}
print(updated_params)
# {'LAYERS', 'UNITS'}

# DICTIONARY CREATION USING zip()

# Lists representing years and corresponding dataset sizes
years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]

# Convert paired elements into dictionary mapping years to dataset sizes
data_growth = dict(zip(years, dataset_sizes))
print(data_growth)
# {2020: 10000, 2021: 25000, 2022: 50000}

# Sales data for different years
sales = {2022: 50000, 2023: 75000, 2024: 100000}

# Calculate profit as 15% of revenue for each year
profit = {year: revenue * 0.15 for year, revenue in sales.items()}
print(profit)
# {2022: 7500.0, 2023: 11250.0, 2024: 15000.0}
