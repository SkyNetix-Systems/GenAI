# -------------------------------
# Zero-Shot Prompting Example
# -------------------------------

# Load environment variables from the .env file
from dotenv import load_dotenv

# Import the OpenAI-compatible client (works with Gemini using base_url)
from openai import OpenAI

# Used to read environment variables like GEMINI_API_KEY
import os

# Load key-value pairs from .env into environment
# Your .env should contain: GEMINI_API_KEY=your_key_here
load_dotenv()

# Read the Gemini API key from environment variables
gemini_key = os.getenv("GEMINI_API_KEY")

# Create an OpenAI client that points to Google's Gemini API endpoint
client = OpenAI(
    api_key=gemini_key,   # ← no hardcoded keys, only .env
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero-Shot Prompting:
# The model is given instructions but NO examples.
SYSTEM_PROMPT = (
    "You should only answer coding-related questions. "
    "If the user asks anything else, just say sorry. "
    "Your name is Alexa."
)

# Sending the request to the Gemini model
response = client.chat.completions.create(
    model="gemini-2.5-flash",     # Gemini model
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },    # System instructions
        { "role": "user", "content": "Hey, can you write Python code to for fibonacci numbers" }
    ]
)

# Output the model's response
print(response.choices[0].message.content)

# NOTE:
# Zero-Shot Prompting = directly asking a question without showing examples.
