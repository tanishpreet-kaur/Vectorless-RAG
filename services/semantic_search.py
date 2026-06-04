from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from langfuse import observe

embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

@observe
def semantic_search(query: str, nodes: list, top_k: int = 5):

    if not nodes:
        return []

    query_embedding = embedding_model.encode(
        query,
        convert_to_tensor=True
    )

    node_texts = []

    for node in nodes:
        title = node.get("title", "")
        summary = node.get("summary", "")
        text = f"""
        Title: {title}

        Summary:
        {summary}
        """
        node_texts.append(text)

    node_embeddings = embedding_model.encode(
        node_texts,
        convert_to_tensor=True
    )

    similarities = cos_sim(
        query_embedding,
        node_embeddings
    )[0]

    ranked = sorted(
        zip(nodes, similarities.tolist()),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]