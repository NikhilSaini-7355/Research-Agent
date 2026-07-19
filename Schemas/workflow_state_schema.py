from typing import TypedDict, List
from Schemas.synthesizer_agent_schema import SynthesizedResearch
from Schemas.TopicAnalysisSchema import TopicAnalysisSchema
from Schemas.PersonaGeneratorSchema import ExpertRolesSchema
from Schemas.outline_schema import OutlineSchema

class WorkflowState(TypedDict):
    job_id: str
    topic: str
    project_id: str
    services: dict

    topic_analysis_response: TopicAnalysisSchema
    personas : ExpertRolesSchema
    search_queries: List[str]
    search_results: List[dict]

    research_summary: str
    outline: OutlineSchema
    
    final_markdown: str                