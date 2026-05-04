from langchain_openai import ChatOpenAI

from src.config import OPENAI_API_KEY


def build_rag_chain(retriever):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY,
    )

    def run(question: str):
        docs = retriever.invoke(question)

        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
        Use o contexto abaixo para responder a pergunta.

        Contexto:
        {context}

        Pergunta:
        {question}
        """

        response = llm.invoke(prompt)

        return response.content, docs

    return run
