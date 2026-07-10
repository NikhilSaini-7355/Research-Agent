from langgraph.graph import StateGraph, START, END
from Schemas.workflow_state_schema import WorkflowState
from Graph.nodes import topic_analyzer_node, persona_generator_node, question_generator_node, search_node, content_extractor_node, embedder_node, synthesizer_node, outline_generator_node, writer_node

workflow = StateGraph(WorkflowState)

# Add your nodes
workflow.add_node("analyze_topic", topic_analyzer_node)
workflow.add_node("generate_persona", persona_generator_node)
workflow.add_node("generate_questions", question_generator_node)
workflow.add_node("search_questions", search_node)
workflow.add_node("extract_content", content_extractor_node)
workflow.add_node("embed_content", embedder_node)
workflow.add_node("synthesize_research", synthesizer_node)
workflow.add_node("generate_outline", outline_generator_node)
workflow.add_node("write", writer_node)

# Define the basic linear flow (Edges)
workflow.add_edge(START, "analyze_topic")
workflow.add_edge("analyze_topic", "generate_persona")
workflow.add_edge("generate_persona", "generate_questions")
workflow.add_edge("generate_questions", "search_questions")
workflow.add_edge("search_questions", "extract_content")
workflow.add_edge("extract_content", "embed_content")
workflow.add_edge("embed_content", "synthesize_research")
workflow.add_edge("synthesize_research", "generate_outline")
workflow.add_edge("generate_outline", "write")
workflow.add_edge("write", END)

# Compile the graph into an executable application
app = workflow.compile()