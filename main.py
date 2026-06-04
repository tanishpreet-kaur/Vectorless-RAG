from graph.workflow import app
from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()

while True:
    query = input("Query: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = app.invoke({"query": query}, config={"callbacks": [langfuse_handler]})
    print("\nAnswer:")
    print(result["answer"])
    print()