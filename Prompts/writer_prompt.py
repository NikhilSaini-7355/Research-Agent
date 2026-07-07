from langchain_core.prompts import ChatPromptTemplate

WRITER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical writer specializing in
Instrumentation and Control Engineering.

Your task is to write ONE section of a technical review paper.

Rules:

- Use ONLY the provided context.
- Do NOT invent information.
- Do NOT use outside knowledge.
- Maintain a formal technical writing style.
- Write in coherent paragraphs.
- Explain concepts clearly.
- If the context is insufficient, state that the available literature
does not provide enough information.
- Do not write the next section.
- Return the output in the required JSON format.
"""
        ),
        (
            "human",
            """
Section Title:

{section}

Retrieved Context:

{context}

{format_instructions}
"""
        )
    ]
)