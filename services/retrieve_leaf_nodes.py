from utils.semantic_search import semantic_search

def retrieve_leaf_nodes(query: str, root_nodes: list, beam_width: int = 3):
    frontier = root_nodes

    while True:
        ranked_nodes = semantic_search(
            query=query,
            nodes=frontier,
            top_k=beam_width
        )

        selected_nodes = [
            node
            for node, score in ranked_nodes
        ]

        next_level = []
        leaf_nodes = []

        for node in selected_nodes:
            children = node.get("nodes", [])
            if children:
                next_level.extend(children)
            else:
                leaf_nodes.append(node)

        if leaf_nodes:
            return leaf_nodes

        if not next_level:
            return selected_nodes

        frontier = next_level