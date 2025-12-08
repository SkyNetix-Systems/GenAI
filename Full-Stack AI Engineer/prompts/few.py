# -------------------------------
# Few-Shot Prompting Example
# -------------------------------

# Load environment variables from the .env file
from dotenv import load_dotenv

# Import the OpenAI-compatible client (works with Gemini using base_url)
from openai import OpenAI

# Used to read environment variables (like GEMINI_API_KEY)
import os

# Load key-value pairs from .env into environment variables
# .env must contain: GEMINI_API_KEY=your_key_here
load_dotenv()

# Read Gemini API key from environment
gemini_key = os.getenv("GEMINI_API_KEY")

# Create the OpenAI client but configured to talk to Google's Gemini API
client = OpenAI(
    api_key=gemini_key,    # No hardcoded API keys
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Few-Shot Prompting:
# You give the model instructions + examples so it understands the pattern.
SYSTEM_PROMPT = """
You should only answer coding-related questions. Do not answer anything else.
Your name is Alexa. If the user asks something unrelated to coding, reply with 'sorry'.

Rule:
- Strictly follow the JSON output format.

Output Format:
{
 "code": "string" or null,
 "isCodingQuestion": boolean
}

Examples:
Q: Can you explain the a + b whole square?
A: { "code": null, "isCodingQuestion": false }

Q: Hey, write a code in python for adding two numbers.
A: { "code": "def add(a, b):\\n    return a + b", "isCodingQuestion": true }
"""

# Ask the model a new question using Few-Shot Prompting
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },  # Instructions + examples
        { "role": "user", "content": "Hey, write a code to add n numbers in js" }
    ]
)

# Print the model’s JSON output
print(response.choices[0].message.content)

# NOTE:
# Few-Shot Prompting = Giving several examples to teach the model the exact format.
