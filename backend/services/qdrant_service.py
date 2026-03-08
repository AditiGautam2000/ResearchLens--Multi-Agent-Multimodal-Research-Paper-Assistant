from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid


class QdrantService:

    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

    # ---------------- CREATE COLLECTION ----------------

    def create_collection(self, collection_name):

        collections = self.client.get_collections().collections
        names = [c.name for c in collections]

        if collection_name not in names:

            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            )

    # ---------------- INSERT DOCUMENTS ----------------

    def insert_documents(self, collection_name, chunks, embeddings):

        points = []

        for chunk, vector in zip(chunks, embeddings):

            # convert tensor → list if needed
            if hasattr(vector, "tolist"):
                vector = vector.tolist()

            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk.page_content,
                    "source": chunk.metadata.get("source", "")
                }
            )

            points.append(point)

        self.client.upsert(
            collection_name=collection_name,
            points=points
        )

        print(f"Inserted {len(points)} TEXT points into Qdrant")

    # ---------------- GET CLIENT ----------------

    def get_client(self):
        return self.client