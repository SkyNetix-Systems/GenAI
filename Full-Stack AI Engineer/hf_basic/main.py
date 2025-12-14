from transformers import pipeline

# Create a pipeline for multimodal generation:
# "image-text-to-text" = model takes an image + text prompt and returns text.
# We're loading Google's Gemma 3 4B Instruction-Tuned model.
# A pipeline in Hugging Face is a ready-to-use shortcut 
# that bundles a model + tokenizer + preprocessing + postprocessing 
# into one simple function.
# "image-text-to-text" means:
#]👉 You give the model an image + some text,
# 👉 The model returns text (usually an answer, caption, or reasoning).
pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")

# Construct the chat-style message structure the pipeline expects.
messages = [
    {
        "role": "user",   # User message in a chat context
        "content": [
            # First content item: an image URL
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            # Second content item: text prompt asking a question about the image
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]

# Run the pipeline with the message.
# This sends both the image + text question to the model.
result = pipe(text=messages)

# Print the model's response so you can see the answer.
print(result)
