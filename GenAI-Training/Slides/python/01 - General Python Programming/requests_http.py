# The requests Library (HTTP for Humans)
import requests
import httpx

# Define the URL for the API request
url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'

# Make a GET request using the requests library
response = requests.get(url)

# Print the HTTP status code of the response
print(response.status_code)

# Print the response headers
print(response.headers)

# Print the raw text content of the response
print(response.text)

# Parse the JSON response into a Python dictionary
data = response.json()

# Access and print the hourly temperature data
print(data['hourly']['temperature_2m'])

# Make a GET request using the httpx library
r = httpx.get(url)

# Print the HTTP status code of the httpx response
print(r.status_code)

# Print the JSON content of the httpx response
print(r.json())