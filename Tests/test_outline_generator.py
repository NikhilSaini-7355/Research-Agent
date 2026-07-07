from Agents.outline_generator import OutlineGenerator
from Agents.synthesizer_agent import SynthesizerAgent

query = "Benefits AI has given to the US Citizens"
topic="AI in USA"

synthesizer = SynthesizerAgent()
research_summary = synthesizer.synthesize_research_summary(query, topic)

generator = OutlineGenerator()

outline = generator.generate_outline(research_summary)

print(outline.model_dump())