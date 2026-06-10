import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="new_articles")

# Query the database
results = collection.query(
    query_texts=["who won bengal elections 2026? Explain in detail"],
    n_results=10 # Number of top matching chunks you want to retrieve
)

# Print the retrieved content
for i, doc in enumerate(results["documents"][0]):
    print(f"\n--- Match {i+1} ---")
    print(f"ID: {results['ids'][0][i]}")
    print(f"Content: {doc}")
    if results["metadatas"][0]:
        print(f"Metadata: {results['metadatas'][0][i]}")