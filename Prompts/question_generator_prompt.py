from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompt_values import ChatPromptValue


from langchain_core.prompts import ChatPromptTemplate

QuestionGeneratorTemplate = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a senior research analyst and subject matter expert.

            Your task is to generate EXACTLY 2 high-quality research questions.

            Requirements:
            - Questions must align with the assigned research dimension.
            - Questions should explore different aspects of the dimension.
            - Questions must be specific, analytical, and research-oriented.
            - Avoid broad, generic, or repetitive questions.
            - Avoid yes/no questions.
            - Avoid generating questions that overlap with each other.
            - Focus on producing questions that would help build a comprehensive research report.

            Research Dimension Guidelines:

            1. Fundamentals and Core Concepts
               - Focus on principles, concepts, definitions, and underlying mechanisms.

            2. Technical and Mathematical Foundations
               - Focus on algorithms, mathematical models, equations, optimization methods, and theoretical analysis.

            3. System Architecture and Components
               - Focus on system structure, components, design choices, and interactions.

            4. Implementation and Practical Deployment
               - Focus on implementation challenges, deployment strategies, tuning, maintenance, and operational considerations.

            5. Applications and Industrial Use Cases
               - Focus on real-world usage, case studies, benefits, industry adoption, and performance improvements.

            6. Challenges, Limitations, and Risks
               - Focus on constraints, bottlenecks, weaknesses, scalability issues, safety concerns, and trade-offs.

            7. Future Trends and Research Directions
               - Focus on emerging technologies, recent advancements, open research problems, and future developments.

            The generated questions must remain strictly within the assigned research dimension.

            Do NOT generate questions that belong to another research dimension.
            
            Examples:
            
            Fundamentals:
            - definitions
            - concepts
            - principles
            - historical development
            
            Technical Foundations:
            - mathematics
            - optimization
            - algorithms
            - theoretical analysis
            
            Implementation:
            - deployment
            - tuning
            - maintenance
            - engineering challenges
            
            Applications:
            - industrial use cases
            - business impact
            - performance improvements
            
            Future Trends:
            - emerging technologies
            - research directions
            - AI integration
            - future developments

            Generate EXACTLY 2 questions.
            """
        ),
        (
            "human",
            """
            Topic: {topic}

            Expert Role: {role}

            Expertise: {expertise}

            Research Dimension: {research_dimension}

            Perspective: {perspective}
            """
        )
    ]
)


def generate_questions_prompt(
    topic: str,
    role: str,
    expertise: str,
    research_dimension: str,
    perspective: str
) -> ChatPromptValue:

    return QuestionGeneratorTemplate.invoke(
        {
            "topic": topic,
            "role": role,
            "expertise": expertise,
            "research_dimension": research_dimension,
            "perspective": perspective,
        }
    )