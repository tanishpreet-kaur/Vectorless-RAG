from services.pdf_retriever import retrieve_pages

def retrieve(state):
    context = retrieve_pages(
        state["leaf_nodes"]
    )

    return {
        "context": context
    }