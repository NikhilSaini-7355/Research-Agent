from src.exception import CustomException
from src.logger import logging
import sys 
import json

from Agents.persona_generator import persona_generator

Topic =  "India vs China economic comparison"

subtopics = [
    "GDP Comparison",
    "Trade Relations",
    "Investment Climate",
    "Poverty Alleviation",
    "Infrastructure Development",
    "Economic Reforms"
  ]

try:
    generator = persona_generator()
    personas = generator.generate_persona(Topic, subtopics)
    logging.info("Persona generation completed successfully.")
    print(json.dumps(personas, indent=2))


except Exception as e:
    logging.error("An error occurred while generating personas.")
    print(CustomException(e, sys))