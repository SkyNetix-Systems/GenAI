#  Using __name__ == '__main__' for Modular and Reusable Code

# preprocess_data.py
def clean_text(text):
    """Lowercase the text and remove special characters."""
    # Basic text cleaning steps
    return text.lower()

def tokenize_text(text):
    """Split text into tokens."""
    # Tokenization steps
    return text.split()

if __name__ == '__main__':
    # Sample text to demonstrate the functions
    sample_text = 'Hello, GenAI World!'
    clean_sample = clean_text(sample_text)
    tokens = tokenize_text(clean_sample)
    print(f'Tokenized text: {tokens}')
