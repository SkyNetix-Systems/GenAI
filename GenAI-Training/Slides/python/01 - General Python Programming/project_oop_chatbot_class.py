from openai import OpenAI

class ChatBot:
    def __init__(self, api_key, model='gpt-4o-mini', temperature=0.5):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def ask(self, user_message):
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

api_key = 'sk-eDToO6CmacP737BR6QpHjGoBPkWSUrdQ3QjzOihbODT3BlbkFJggJyH68QhBE4adkVdKpxG_LcifC8g7Jnedak9IdD4A'
bot = ChatBot(api_key=api_key, temperature=0.7)
response = bot.ask('What are some groundbreaking AI advancements?')
print(response)
