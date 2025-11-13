# Class Blueprint:
# - API Key Attribute: Stores the API key for authentication.
# - ask() Method: Sends user messages to the OpenAI API and retrieves responses.
# - Model and Temperature Attributes: Allows control over the model type and response randomness.
from openai import OpenAI

class ChatBot:
    """A chatbot that interacts with the OpenAI API to generate responses."""
    def __init__(self, api_key, model='gpt-4o-mini', temperature=0.5):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature


    def ask(self, user_message):
       """Sends a message to the OpenAI API and retrieves the response."""
       try:
           client = OpenAI(api_key=self.api_key)
           response = client.chat.completions.create(
               model=self.model,
               messages=[
                   {'role': 'user', 'content': user_message}
               ],
               temperature=self.temperature
           )
           return response.choices[0].message.content
       except Exception as e:
           return f'An error occurred: {e}'


api_key = 'sk-eDToO6macP737BR6QpHBPkWSUrdQ3QjzOihbODT3BlbkFJggKG_LcifC8g7Jnedak9IdD4A'
bot = ChatBot(api_key=api_key, temperature=0.7)
response = bot.ask('What are some groundbreaking AI advancements?')
print(response)

# Additional Customizations:
# 1. **Save Responses to a File**
# 2. **Load Conversation History**
# 3. **Log Errors to a File**
# 4. **Enable Contextual Conversations**
# 5. **Export Responses as JSON**
# 6. **Integrate with External APIs**
