from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.document_loader import load_pdf
from src.chunking import split_documents
from src.embeddings import get_embeddings
from src.vector_store import get_vector_store

def ingest(file_path):
    documents = load_pdf(file_path)
    chunks = split_documents(documents)

    embeddings = get_embeddings()
    vector_store = get_vector_store(embeddings)

    vector_store.add_documents(chunks)

    print(f"Ingested {len(chunks)} chunks")

if __name__ == "__main__":
    ingest("data/raw/sample.pdf")
