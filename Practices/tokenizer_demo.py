import torch                              # python libraies 
import torch.nn as nn                      # -> nn = neural network module
from transformers import AutoTokenizer      # -> AutoTokenizer = Hugging Face's library for tokenization, which provides pre-trained tokenizers for various models.

# STEP 1: INPUT TEXT
text = "I love learning AI"


# STEP 2: TOKENIZATION
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

tokens = tokenizer.tokenize(text)      # -> Tokenize the input text into individual tokens (e.g., words or subwords) using the BERT tokenizer.

token_ids = tokenizer.encode(text, return_tensors="pt")    # -> Convert the input text into token IDs (numerical representations of tokens) and return them as a PyTorch tensor.

print("TOKENS:", tokens)
print("TOKEN IDS:", token_ids)


# STEP 3: EMBEDDINGS  --> covert word into vector form 

embeddings = embedding_layer(token_ids)  # GENERATE EMBEDDINGS for the token IDs using an embedding layer. The embedding layer maps each token ID to a dense vector representation, which captures semantic information about the token. The resulting embeddings will have a shape of (batch_size, sequence_length, embedding_dim), where embedding_dim is the size of the embedding vectors (e.g., 8 in this case).

print("\nEMBEDDINGS:")
print(embeddings.shape)


# STEP 4: POSITIONAL ENCODING
position = torch.arange(token_ids.size(1)).unsqueeze(0)

position_embedding = nn.Embedding(512, 8)

pos_embeddings = position_embedding(position)

final_embeddings = embeddings + pos_embeddings

print("\nPOSITIONAL ENCODING ADDED:")
print(final_embeddings.shape)


# STEP 5: SELF ATTENTION
attention = nn.MultiheadAttention(embed_dim=8, num_heads=2, batch_first=True)

attention_output, attention_weights = attention(
    final_embeddings,
    final_embeddings,
    final_embeddings
)

print("\nSELF ATTENTION OUTPUT:")
print(attention_output.shape)


# STEP 6: FEED FORWARD NETWORK
feed_forward = nn.Sequential(
    nn.Linear(8, 16),
    nn.ReLU(),
    nn.Linear(16, 8)
)

ffn_output = feed_forward(attention_output)

print("\nFEED FORWARD OUTPUT:")
print(ffn_output.shape)


# STEP 7: FINAL OUTPUT
output_layer = nn.Linear(8, 30522)

final_output = output_layer(ffn_output)

print("\nFINAL OUTPUT:")
print(final_output.shape)