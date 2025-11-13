# PARSING JSON DATA FROM API RESPONSES

import json
import requests

# Define the API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the API
response = requests.get(url)

# Parse the JSON response into a Python list of dictionaries
posts_data = json.loads(response.text)
print(posts_data)

# Iterate through the list and print each post
for item in posts_data:
    print(item)

print(posts_data[0]['title'])

# Example of a JSON response containing API usage details and choices
response = {
    "usage": {
        "total_tokens": 1000,
        "details": {"prompt_tokens": 300, "completion_tokens": 700}
    },
    "choices": [
        {"text": "The capital of France is Paris.", "index": 0},
        {"text": "France's capital is Paris.", "index": 1}
    ]
}

total_tokens = response["usage"]["total_tokens"]
print(total_tokens)

choice_texts = [choice["text"] for choice in response["choices"]]
print(choice_texts)
