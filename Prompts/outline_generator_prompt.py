from langchain_core.prompts import ChatPromptTemplate

OUTLINE_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical paper planner specializing in
Instrumentation and Control Engineering.

Generate a logical review paper outline.

Rules:
- Use ONLY the provided research summary.
- Do not invent new topics.
- Include Introduction and Conclusion.
- Include Mathematical Foundations if applicable.
- Include Industrial Applications if applicable.
- Include Future Research Directions if applicable.

Return the response in the required JSON format.
"""
        ),
        (
            "human",
            """
Research Summary:

{research_summary}

{format_instructions}
"""
        )
    ]
)