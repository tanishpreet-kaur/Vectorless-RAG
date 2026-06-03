import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

JSON_PATH = Path("data/govt_law_chpt_10_structure.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    hierarchy = json.load(f)


embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def semantic_search(query: str, nodes: list, top_k: int = 3):
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
        node_texts.append(
            f"""
            Title: {title}

            Summary:
            {summary}
            """
        )

    node_embeddings = embedding_model.encode(
        node_texts,
        convert_to_tensor=True
    )

    scores = cos_sim(
        query_embedding,
        node_embeddings
    )[0]

    ranked = sorted(
        zip(nodes, scores.tolist()),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]