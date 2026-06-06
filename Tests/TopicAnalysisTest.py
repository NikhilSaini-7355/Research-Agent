import sys
import os

# Get the absolute path of the parent directory (project root) and add it to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Agents.TopicAnalyzerAgent import TopicAnalyzerAgent

TopicAnalyzerObj = TopicAnalyzerAgent()

result = TopicAnalyzerObj.analyze("India vs China economic comparison")

result_dict = result.model_dump()

result_json = result.model_dump_json(indent=2)
print(result_json)