from LLM.groq_client import llm
import json

def generate_questions(topic, persona):

    prompt = f"""
    Topic: {topic}
    
    Role: {persona['role']}
    
    Perspective: {persona['perspective']}
    
    Generate 5 research questions that this persona would ask.
    Return only a JSON array.
    Example:
    [
      "What are the benefits of AI diagnosis?",
      "How accurate are AI systems?"
    ]

    You must respond ONLY with raw, valid JSON. Do not include markdown formatting, backticks, or conversational text. Start your response directly with the JSON array. Ensure the JSON is properly formatted and can be parsed without errors.
    """

    response = llm.invoke(prompt)

    return json.loads(response.content)