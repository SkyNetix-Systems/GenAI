# Load the load_dotenv function from the python-dotenv package.
# This function reads your .env file and sets the environment variables.
from dotenv import load_dotenv

# Import the OpenAI client class from the official OpenAI Python SDK.
from openai import OpenAI

# This loads all key=value pairs from the .env file into your environment.
# Example: OPENAI_API_KEY=your_key
load_dotenv()

# Create an OpenAI client instance.
# It automatically picks up OPENAI_API_KEY from your environment.
client = OpenAI()

# Send a chat completion request to the OpenAI API.
response = client.chat.completions.create(
    model="gpt-4o-mini",    # The LLM you want to use
    messages=[              # Chat history as a list of messages
        {
            "role": "user", 
            "content": "Hey, I am Akhilesh, Nice to meet you"
        }
    ]
)

# Print the model's reply message to the console.
# response.choices is a list → first choice → message → content
print(response.choices[0].message.content)
