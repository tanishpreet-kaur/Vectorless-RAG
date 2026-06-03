from typing import TypedDict
from langchain_core.documents import Document

class RAGState(TypedDict):
    query: str
    leaf_nodes: list
    retrieved_pages: list[Document]
    chunks: list[Document]
    reranked_docs: list[Document]
    answer: str