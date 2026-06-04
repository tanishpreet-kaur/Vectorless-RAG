from typing import TypedDict

class RAGState(TypedDict):
    query: str
    leaf_nodes: list
    context: str
    answer: str