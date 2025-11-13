# JSON HANDLING FOR STRUCTURED DATA

import json  # Importing the JSON module

# Reading and parsing a JSON file
with open('config.json') as file:
    config = json.load(file)  # Load JSON content into a Python dictionary

# Print the raw JSON data as a dictionary
print(config)

# Formatting JSON for better readability
pretty_json = json.dumps(config, indent=4)  # Convert dictionary to a formatted JSON string
print(pretty_json)

# Accessing nested values from the JSON structure
print(config['api_settings']['endpoint'])  # Retrieves the 'endpoint' from 'api_settings'
