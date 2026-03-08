from backend.tools.clip_text_embedding import get_text_embedding

text = "A diagram of a neural network"

embedding = get_text_embedding(text)

print("Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])