from pathlib import Path
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.embeddings import get_embeddings
from src.vector_store import get_vector_store
from src.retriever import get_retriever
from src.rag_chain import build_rag_chain

st.title("RAG Production Learning")

question = st.text_input("Faça sua pergunta")

if question:
    embeddings = get_embeddings()
    vector_store = get_vector_store(embeddings)
    retriever = get_retriever(vector_store)
    rag = build_rag_chain(retriever)

    answer, docs = rag(question)

    st.write("### Resposta")
    st.write(answer)

    st.write("### Fontes")
    for doc in docs:
        st.write(doc.metadata)
