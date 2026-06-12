from src.exception import CustomException
from src.logger import logging
import sys 
import json

from Agents.persona_generator import PersonaGenerator
from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

TopicAnalyzerObj = TopicAnalyzerAgent()

topic =  "Explain Model Predictive Control"

analysis_response = TopicAnalyzerObj.analyze(topic)

try:
    generator = PersonaGenerator()
    personas = generator.generate_persona(analysis_response)
    logging.info("Persona generation completed successfully.")
    personas = personas.model_dump()  # Convert to dictionary if it's a Pydantic model
    print(json.dumps(personas, indent=2))

except Exception as e:
    logging.error("An error occurred while generating personas.")
    print(CustomException(e, sys))

