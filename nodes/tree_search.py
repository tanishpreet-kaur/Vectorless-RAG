from services.hierarchy_loader import load_hierarchy
from services.retrieve_leaf_nodes import retrieve_leaf_nodes

hierarchy = load_hierarchy("data/govt_law_chpt_10_structure.json")

def tree_search(state):
    ranked_leaf_nodes = retrieve_leaf_nodes(
        query=state["query"],
        root_nodes=hierarchy["structure"],
        beam_width=5
    )

    leaf_nodes = [
        node
        for node, score in ranked_leaf_nodes
    ]

    return {
        "leaf_nodes": leaf_nodes
    }