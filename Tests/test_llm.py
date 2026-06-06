from dotenv import load_dotenv
#import os

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

response = llm.invoke(
    "Explain what Artificial Intelligence is in 50 words."
)

print(response.content)