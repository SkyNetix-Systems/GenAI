from openai import OpenAI
from dotenv import load_dotenv
import requests

# Load environment variables from .env file (e.g., your OPENAI_API_KEY)
load_dotenv()

# Create an OpenAI client instance to talk to the API
client = OpenAI()



def main():
    # Take user input from terminal
    user_query = input("> ")
    
    # Send user query to OpenAI Chat Completion API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            { "role": "user", "content": user_query }
        ]
    )

    # Print AI's response
    print(f"🤖: {response.choices[0].message.content}")

# Run the main function
main()
