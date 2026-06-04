from graph.workflow import app

while True:
    query = input("Query: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = app.invoke({"query": query})
    print("\nAnswer:")
    print(result["answer"])
    print()