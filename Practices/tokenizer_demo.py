from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = [
    "I am akshat"
    "me akshat hu"
    "chatgpt is amazing"
    "supercalifragilisticexpialidocious"
]

for text in text:
    tokens = tokenizer.tokenize(text)
    ids = tokenizer.encode(text)
    print(f"Text: {text}")
    print(f"Tokens: {tokens}")
    print(f"IDs: {ids}")
    print(f"Count: {len(tokens)} tokens")