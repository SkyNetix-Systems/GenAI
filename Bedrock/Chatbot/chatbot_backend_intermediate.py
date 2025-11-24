from langchain_aws import ChatBedrockConverse

def demo_chatbot(message_text: str):
    llm = ChatBedrockConverse(
        credentials_profile_name="default",
        model="amazon.titan-text-lite-v1",   # <-- change to a model *you actually have access to*
        temperature=0.1,
        max_tokens=200
    )

    messages = [
        {"role": "user", "content": [{"text": message_text}]}
    ]

    return llm.invoke(messages)

# ---- Test ----
resp = demo_chatbot("What is Amazon Bedrock?")
#print(type(resp))
#print(dir(resp))

print(resp.content)
