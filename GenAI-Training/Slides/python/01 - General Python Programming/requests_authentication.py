# Managing HTTP Authentication and Headers: OpenAI API

import requests

# Change this key to your own from https://platform.openai.com/docs/overview
# Don't hard-code API keys in real-world projects!!! Use environment variables instead.
api_key = 'sk-proj-0slq8k-6DnoZYkg64eMeBUd14rrtEGQ6txaSZbMPSZ4n5PXuvsv_VOfqDXRqET_0A'
# OpenAI API endpoint
url = 'https://api.openai.com/v1/chat/completions'

# Headers for the API request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Request payload
data = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'What do you think are the most important inventions of the 21st century?'}
    ],
    'temperature': 0.7
}

# Making the API request
try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Extract and print the assistant's reply
    result = response.json()
    reply = result.get('choices', [{}])[0].get('message', {}).get('content', 'No response received.')
    print(f'Assistant: {reply}')

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except requests.exceptions.RequestException as req_err:
    print(f'Request error occurred: {req_err}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
