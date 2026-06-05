from services.semantic_search import semantic_search
from langfuse import observe

@observe
def retrieve_leaf_nodes(
    query: str,
    root_nodes: list,
    beam_width: int = 3
):
    frontier = root_nodes
    all_leaf_nodes = []

    while frontier:
        ranked_nodes = semantic_search(
            query=query,
            nodes=frontier,
            top_k=beam_width
        )
        next_level = []
        for node, score in ranked_nodes:
            children = node.get("nodes", [])
            if children:
                next_level.extend(children)
            else:
                all_leaf_nodes.append(
                    (node, score)
                )
        frontier = next_level

    return sorted(
        all_leaf_nodes,
        key=lambda x: x[1],
        reverse=True
    )