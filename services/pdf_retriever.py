from langchain_community.document_loaders import PyPDFLoader

PDF_PATH = "data/govt_law_chpt_10.pdf"
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


def retrieve_pages(nodes):
    context = []

    for node in nodes:
        page_text = extract_pdf_pages(
            PDF_PATH,
            node["start_index"],
            node["end_index"]
        )

        context.append(
            f"""
            Title: {node['title']}

            Pages:
            {node['start_index']} - {node['end_index']}

            Content:
            {page_text}
            """
        )

    return "\n\n".join(context)