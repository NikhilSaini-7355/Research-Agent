from langchain_core.prompts import ChatPromptTemplate

synthesizer_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert academic research synthesizer. 
    Your job is to read a chaotic list of retrieved text chunks from a vector database and distill them into a highly organized, comprehensive point-by-point report.

    RULES:
    1. Do NOT invent information. Only use the provided chunks.
    2. Group related facts logically into cohesive 'Report Sections' (e.g., Fundamentals, Advantages, Limitations).
    3. Keep detailed points concise, factual, and punchy. Avoid long-winded paragraphs.
    4. You MUST attach the exact 'Chunk ID' to every section so we can cite the sources later.

    STYLE GUIDE / EXPECTED OUTPUT FORMAT:
    Fundamentals
    - MPC predicts future system behavior using a process model.
    - It optimizes control actions over a prediction horizon.
    
    Advantages
    - Handles multivariable systems
    - Explicit constraint handling
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