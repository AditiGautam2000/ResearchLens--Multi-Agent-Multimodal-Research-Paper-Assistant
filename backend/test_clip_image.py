from backend.tools.image_analyzer import get_image_embedding

image_path = "backend/me.jpeg"

embedding = get_image_embedding(image_path)

print("Embedding length:", len(embedding))
print("First 10 values:", embedding[:10])