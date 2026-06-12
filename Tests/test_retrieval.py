from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Same embedding model used during indexing
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Connect to existing Chroma DB
vectorstore = Chroma(
    collection_name="new_articles",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

query = (
    "What factors led to BJP victory "
    "in Bengal elections 2026?"
)

results = vectorstore.similarity_search_with_score(
    query=query,
    k=10
)

for i, (doc, score) in enumerate(results, start=1):
    print("\n" + "=" * 100)
    print(f"MATCH #{i}")
    print("=" * 100)

    print(f"Score: {score}")

    print("\nMetadata:")
    for key, value in doc.metadata.items():
        print(f"{key}: {value}")

    print("\nContent:")
    print(doc.page_content[:1500])