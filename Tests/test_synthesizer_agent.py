
from Agents.synthesizer_agent import SynthesizerAgent


try:
    query = "Benefits AI has given to the US Citizens"
    topic="AI in USA"
    
    synthesizer = SynthesizerAgent()
    research_summary = synthesizer.synthesize_research_summary(query, topic)
    print(research_summary)

except Exception as e:
    logging.error("An error occurred while generating the report.")
    print(CustomException(e, sys))