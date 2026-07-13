# File: Tests/test_personaGenerator.py
import sys
import os
import asyncio

# Ensure Python finds all your top-level folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.exception import CustomException
from src.logger import logging
from Agents.persona_generator import PersonaGenerator
from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

async def check_persona_generator_node():
    try:
        print("🚀 Starting Topic Analysis...")
        TopicAnalyzerObj = TopicAnalyzerAgent()
        topic = "Explain Model Predictive Control"
        analysis_response = TopicAnalyzerObj.analyze(topic)
        print("✅ Topic Analysis Complete.")

        print("🚀 Generating Personas...")
        generator = PersonaGenerator()
        personas = await generator.generate_persona(analysis_response, "21111111-1111-1111-1111-111111111111")
        
        logging.info("Persona generation completed successfully.")
        print("\n--- GENERATED EXPERTS ---")
        for expert in personas.experts:
            print(f"Role: {expert.role}")
            print(f"Expertise: {expert.expertise}")
            print(f"Research Dimension: {expert.research_dimension}")
            print(f"Perspective: {expert.perspective}\n")

    except Exception as e:
        logging.error("An error occurred while generating personas.")
        print(CustomException(e, sys))

if __name__ == "__main__":
    asyncio.run(check_persona_generator_node())