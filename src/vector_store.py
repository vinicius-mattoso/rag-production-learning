from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from src.config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION


def get_qdrant_client():
    return QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )


def get_vector_store(embeddings):
    client = get_qdrant_client()

    return QdrantVectorStore(
        client=client,
        collection_name=QDRANT_COLLECTION,
        embedding=embeddings,
    )