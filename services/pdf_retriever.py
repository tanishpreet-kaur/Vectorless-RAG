from langchain_community.document_loaders import PyPDFLoader
from langfuse import observe

PDF_PATH = "data/govt_law_chpt_10.pdf"

@observe
def extract_pdf_pages(pdf_path, start_page, end_page):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    total_pages = len(docs)
    if start_page < 1 or end_page > total_pages:
        return ""
    selected_docs = docs[start_page - 1:end_page]
    stored_data = ""
    for doc in selected_docs:
        stored_data += doc.page_content + "\n\n"
    return stored_data

@observe
def retrieve_pages(nodes):
    context = []
    seen = set()
    for node in nodes:
        page_range = (
            node["start_index"],
            node["end_index"]
        )
        if page_range in seen:
            continue
        seen.add(page_range)
        page_text = extract_pdf_pages(
            PDF_PATH,
            node["start_index"],
            node["end_index"]
        )
        context.append(
            f"""
            Title: {node['title']}
            Pages: {node['start_index']} - {node['end_index']}
            Content: {page_text}
            """
        )
    return "\n\n".join(context)