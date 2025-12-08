# Load variables from .env
from dotenv import load_dotenv

# Official Google Gemini SDK
import google.generativeai as genai

# For reading environment variables
import os

# Load .env file
load_dotenv()

# Get key from .env file
gemini_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini with your API key
genai.configure(api_key=gemini_key)

# Create a model instance
model = genai.GenerativeModel("gemini-2.5-flash")

# Send prompt to Gemini
response = model.generate_content("Explain how AI works in a few words")

# Print model output
print(response.text)
