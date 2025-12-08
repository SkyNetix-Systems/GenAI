# Simple Chain of Thought Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load .env for API key
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask a math question and request step-by-step reasoning
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Explain your steps clearly before giving the final answer."
        },
        {
            "role": "user",
            "content": "Solve 2 + 3 * 4"
        }
    ]
)

# Print the model's answer
print(response.choices[0].message.content)
