from LLM.groq_client import llm
from Prompts.TopicAnalysisPrompt import generate_topic_analysis_prompt
from Schemas.TopicAnalysisSchema import TopicAnalysisSchema

class TopicAnalyzerAgent:

    def analyze(self, topic: str):

        prompt = generate_topic_analysis_prompt(topic)

        structured_llm = llm.with_structured_output(TopicAnalysisSchema)

        result = structured_llm.invoke(prompt)

        # print(result)
        
        return result