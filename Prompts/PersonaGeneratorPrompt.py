from langchain_core.prompts import ChatPromptTemplate

PersonaGeneratorPrompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert research planner.

            Your task is to create EXACTLY 5 expert personas.

            Each expert must be responsible for ONE unique research dimension.

            Required research dimensions:

            1. Fundamentals and Core Concepts
            2. Technical and Mathematical Foundations
            3. Implementation and Practical Deployment
            4. Applications and Industrial Use Cases
            5. Future Trends and Research Directions

            Requirements:

            - Generate exactly one expert per dimension.
            - Each expert should have a unique role.
            - Each expert should have a unique expertise area.
            - Each expert should provide a different perspective.
            - The experts should collectively cover the entire topic.
            - Do not create overlapping personas.

            For each expert generate:

            - role
            - expertise
            - research_dimension
            - perspective
            """
        ),
        (
            "human",
            """
            Topic: {topic}

            Domain: {domain}

            Difficulty: {difficulty}

            Subtopics:
            {subtopics}

            Keywords:
            {keywords}

            Research Goals:
            {research_goals}
            """
        )
    ]
)

def generate_persona_prompt(
    topic: str,
    domain: str,
    difficulty: str,
    subtopics: list[str],
    keywords: list[str],
    research_goals: list[str]
):

    return PersonaGeneratorPrompt.invoke(
        {
            "topic": topic,
            "domain": domain,
            "difficulty": difficulty,
            "subtopics": "\n".join(subtopics),
            "keywords": "\n".join(keywords),
            "research_goals": "\n".join(research_goals)
        }
    )