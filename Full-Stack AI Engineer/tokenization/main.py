import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Akhilesh"
tokens = enc.encode(text)

# Tokens: [25216, 3274, 0, 3673, 1308, 382, 13232, 71, 2892, 71]
print("Tokens: ", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 13232, 71, 2892, 71])
print("Decoded: ", decoded)