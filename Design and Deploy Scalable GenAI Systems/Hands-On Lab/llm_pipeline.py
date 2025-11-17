import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Template with placeholder
SUMMARY_PROMPT_TEMPLATE = """
You are a helpful assistant. Summarize the following text into 3 concise bullet points:
---
{text}
---
Bullet Points:
"""

def run_summary_pipeline(input_text):
    # Inject user input into the prompt
    prompt = SUMMARY_PROMPT_TEMPLATE.format(text=input_text)

    # Call OpenAI's Chat Completions API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use gpt-4o / gpt-4.1 / gpt-4o-mini
        messages=[
            {"role": "system", "content": "You are a summarization assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("Paste your text below to summarize:\n")
    user_input = input()
    output = run_summary_pipeline(user_input)
    print("\n🧠 Summary:\n", output)
