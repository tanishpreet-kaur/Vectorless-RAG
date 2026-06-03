from utils.retrieve_leaf_nodes import retrieve_leaf_nodes

def tree_search(state):
    query = state["query"]

    leaf_nodes = retrieve_leaf_nodes(
        query=query,
        root_nodes=hierarchy["structure"],
        beam_width=3
    )

    for node in leaf_nodes:
        print(node["title"])

    return {
        "leaf_nodes": leaf_nodes
    }