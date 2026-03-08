from langchain_ollama import OllamaEmbeddings

embeddings_model = OllamaEmbeddings(model="nomic-embed-text")


def generate_embedding(text: str):

    embedding = embeddings_model.embed_query(text)

    return embedding