#  Project: Making an API Request to OpenAI

import requests
import json

# Change this key to your own from https://platform.openai.com/docs/overview
# Don't hard-code API keys in real-world projects!!! Use environment variables instead.
api_key = 'sk-eDToO6CmacP737BR6QpHjGoBPkW3QjOihbODlbkFJggJyH68QhBE4adkVdKpG_LcifC8g7Jnedak9IdD4A'

# OpenAI API endpoint
url = 'https://api.openai.com/v1/chat/completions'

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Request payload
data = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Give me the most interesting question you have ever been asked.'}
    ],
    'temperature': 0.7
}

# Making the API request
response = requests.post(url, headers=headers, json=data)

# Handling the response
if response.status_code == 200:
    result = response.json()

    # Pretty-print the full JSON response (for debugging)
    print(json.dumps(result, indent=4))

    # Extract and print the assistant's reply
    reply = result['choices'][0]['message']['content']
    print(reply)
    # REPLY:
    # One of the most interesting questions I've encountered is:
    # "If you could create a new sense for humans, what would it be and how would it change
    # our perception of the world?" This question sparks creativity and invites exploration
    # into the nature of human experience and perception, prompting discussions
    # about how such a sense could enhance our understanding of our environment, interactions,
    # and even emotions. It opens up a fascinating dialogue about the limits of human perception
    # and the potential for new ways of experiencing reality.

else:
    print(f'Error: {response.status_code}\n{response.text}')
