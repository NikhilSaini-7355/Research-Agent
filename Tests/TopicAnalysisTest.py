import sys
import json
# import os

# # Get the absolute path of the parent directory (project root) and add it to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)

from src.exception import CustomException
from src.logger import logging


try:
    from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

    TopicAnalyzerObj = TopicAnalyzerAgent()
    
    result = TopicAnalyzerObj.analyze("India vs China economic comparison")
    
    logging.info("Topic Analysis completed successfully.")

    print(json.dumps(result, indent=2))

except Exception as e:
    logging.error("An error occurred while analyzing the topic.")
    print(CustomException(e, sys))