from langgraph.graph import (StateGraph, START, END)
from states.RAGState import RAGState
from nodes.tree_search import tree_search
from nodes.retrieve import retrieve
from nodes.generate_answer import generate_answer

graph = StateGraph(RAGState)

graph.add_node("tree_search", tree_search)
graph.add_node("retrieve", retrieve)
graph.add_node("generate_answer", generate_answer)

graph.add_edge(START, "tree_search")
graph.add_edge("tree_search", "retrieve")
graph.add_edge("retrieve", "generate_answer")
graph.add_edge("generate_answer", END)

app = graph.compile()