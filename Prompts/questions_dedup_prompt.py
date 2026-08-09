from langchain_core.prompts import ChatPromptTemplate

QuestionRefinerTemplate = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a senior research coordinator.

            Your task is to:

            1. Remove duplicate questions.
            2. Merge highly similar questions.
            3. Keep only the most informative questions.
            4. Return between 5 and 8 questions.
            
            {format_instructions}
            """
        ),
        (
            "human",
            """
            Topic: {topic}

            Questions:

            {questions}
            """
        )
    ]
)
def generate_dedup_prompt(
    topic: str,
    questions: list[str],
    format_instructions: str
):
    return QuestionRefinerTemplate.invoke(
        {
            "topic": topic,
            "questions": "\n".join(
                f"- {q}"
                for q in questions
            ),
            "format_instructions": format_instructions
        }
    )