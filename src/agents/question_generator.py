from LLM.groq_client import llm
import json

def generate_questions(topic, persona):

    prompt = f"""
    Topic: {topic}

    Persona: {persona}

    Generate 5 important research questions that this persona would ask.

    Return only a JSON array.

    Example:
    [
      "What are the benefits of AI diagnosis?",
      "How accurate are AI systems?"
    ]
    """

    response = llm.invoke(prompt)

    return json.loads(response.content)


