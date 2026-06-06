from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

TopicAnalysisTemplate = ChatPromptTemplate([
    ('system',"You are a senior research analyst."),
    ('human',"Analyze the topic: {topic} and return: 1. Exact Topic given to you, 2. Domain, 3. Research Type, 4. Difficulty, 5. Important Subtopics, 6. Keywords, 7. Research Goals. Return ONLY valid JSON.")
])

def generate_topic_analysis_prompt(topic: str) -> str:
    prompt = TopicAnalysisTemplate.invoke({'topic': topic})
    return prompt

