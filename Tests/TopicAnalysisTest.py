import sys
import os

# Get the absolute path of the parent directory (project root) and add it to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.exception import CustomException
from src.logger import logging


try:
    from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

    TopicAnalyzerObj = TopicAnalyzerAgent()
    
    result = TopicAnalyzerObj.analyze("India vs China economic comparison")
    
    result_dict = result.model_dump()
    
    result_json = result.model_dump_json(indent=2)
    logging.info("Topic analysis completed successfully.")
    print(result_json)

except Exception as e:
    logging.error("An error occurred while analyzing the topic.")
    print(CustomException(e, sys))