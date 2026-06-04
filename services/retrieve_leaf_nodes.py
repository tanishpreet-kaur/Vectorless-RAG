from services.semantic_search import (
    semantic_search
)
from langfuse import observe

@observe
def retrieve_leaf_nodes(
    query: str,
    root_nodes: list,
    beam_width: int = 3
):
    """
    Traverse hierarchy level by level.

    Returns:
        [
            (leaf_node, score),
            (leaf_node, score)
        ]
    """

    frontier = root_nodes

    while True:

        ranked_nodes = semantic_search(
            query=query,
            nodes=frontier,
            top_k=beam_width
        )

        next_level = []

        leaf_nodes = []

        for node, score in ranked_nodes:

            children = node.get("nodes", [])

            if children:

                next_level.extend(children)

            else:

                leaf_nodes.append(
                    (node, score)
                )

        if leaf_nodes:

            return sorted(
                leaf_nodes,
                key=lambda x: x[1],
                reverse=True
            )

        if not next_level:

            return ranked_nodes

        frontier = next_level