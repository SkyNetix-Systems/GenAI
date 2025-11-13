# Handling HTTP Errors
import json
import requests

try:
    # Define the URL for the API request
    url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'

    # Make the GET request with a timeout of 5 seconds
    response = requests.get(url, timeout=5)

    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()  # This will raise an exception if the response status code indicates an error

    # If the request was successful, parse the JSON response and print it with indentation
    print(json.dumps(response.json(), indent=4))

except requests.exceptions.RequestException as e:
    # Catch any requests-related exceptions (e.g., network errors, timeouts, bad status codes)
    print(f'An error occurred: {e}')