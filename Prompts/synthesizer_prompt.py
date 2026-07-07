from langchain_core.prompts import ChatPromptTemplate

synthesizer_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert academic research synthesizer. 
            Your job is to read a chaotic list of retrieved text chunks from a vector database 
            and distill them into a highly organized, factual summary.
            
            RULES:
            1. Do NOT invent information. Only use the provided chunks.
            2. Merge duplicate facts into a single 'Key Finding'.
            3. You MUST attach the exact 'Chunk ID' to every fact so we can cite it later.
            """),
            ("human", "Research Topic: {topic}\n\nRetrieved Chunks:\n{raw_chunks}")
        ])

def generate_synthesizer_prompt(topic: str, retrieved_data: list):
    formatted_chunks = ""
    for item in retrieved_data:
        formatted_chunks += f"[ID: {item['id']}]\nText: {item['text']}\n\n"

    print(f"🧠 Synthesizing {len(retrieved_data)} chunks for topic: {topic}...")

    return synthesizer_prompt.invoke(
        {
            "topic": topic,
            "raw_chunks": formatted_chunks
        }
    )