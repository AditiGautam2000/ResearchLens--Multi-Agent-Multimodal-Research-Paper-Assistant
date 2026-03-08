"""# backend/tools/vector_search.py

from backend.services.qdrant_service import QdrantService
from backend.tools.embedding_generator import generate_embedding
from backend.tools.clip_text_embedding import get_text_embedding


def search_documents(query: str, limit: int = 15):

    qdrant_service = QdrantService()
    client = qdrant_service.get_client()

    embedding = generate_embedding(query)

    results = client.query_points(
        collection_name="text_documents",
        query=embedding,
        limit=limit
    )

    documents = []

    for point in results.points:

        payload = point.payload or {}
        text = payload.get("text")

        if text:
            documents.append(text)

    return documents


def search_images(query: str, limit: int = 5):

    qdrant_service = QdrantService()
    client = qdrant_service.get_client()

    embedding = get_text_embedding(query)

    results = client.query_points(
        collection_name="image_documents",
        query=embedding,
        limit=limit
    )

    images = []

    for point in results.points:

        payload = point.payload or {}
        image_path = payload.get("image_path")

        if image_path:
            images.append(image_path)

    return images"""


from backend.services.qdrant_service import QdrantService
from backend.tools.embedding_generator import generate_embedding


def search_documents(query: str, limit: int = 10):

    qdrant_service = QdrantService()
    client = qdrant_service.get_client()

    embedding = generate_embedding(query)

    results = client.query_points(
        collection_name="your_agent",
        query=embedding,
        limit=limit
    )

    context = []

    for point in results.points:

        payload = point.payload or {}

        text = payload.get("text")

        if text:
            context.append(text)

    return context