# Load environment variables from the .env file
from dotenv import load_dotenv

# Import the OpenAI client (can be used to call Gemini with base_url)
from openai import OpenAI

# Used to read variables from .env
import os

# Load variables from .env (expects GEMINI_API_KEY inside)
load_dotenv()

# Read your Gemini API key
gemini_key = os.getenv("GEMINI_API_KEY")

# Create the OpenAI client, but point it to Google's Gemini API
client = OpenAI(
    api_key=gemini_key,  # using Gemini key
    base_url="https://generativelanguage.googleapis.com/v1beta/"  # Google's endpoint
)

# Ask the Gemini model a question
response = client.chat.completions.create(
    model="gemini-2.5-flash",  # Gemini model name
    messages=[
        { "role": "system", "content": "Sorry, I can only answer maths questions." },
        { "role": "user", "content": "What is (a + b)²?" }
    ]
)

# Print the model's answer
print(response.choices[0].message.content)
