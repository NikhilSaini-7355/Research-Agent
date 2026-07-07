from LLM.groq_client import llm

from Schemas.synthesizer_agent_schema import (
    SynthesizedResearch
)

from Prompts.synthesizer_prompt import (
    generate_synthesizer_prompt
)

class SynthesizerAgent:

    def synthesize_chunks(
        self,
        topic: str,
        retrieved_data: list
    )->SynthesizedResearch:

        prompt = generate_synthesizer_prompt(
            topic=topic,
            retrieved_data=retrieved_data
        )

        structured_llm = llm.with_structured_output(
            SynthesizedResearch
        )

        result = structured_llm.invoke(
            prompt
        )

        return result
