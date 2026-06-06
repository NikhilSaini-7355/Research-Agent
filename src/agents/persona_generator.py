from LLM.groq_client import llm
import json

class persona_generator:

    def generate_persona(self,Topic:str, subtopic:list[str]):

        prompt = f"""
            Topic: {Topic}
            
            Subtopics:
            {subtopic}
            
            Generate 5 expert personas with distinct viewpoints relevant to the topic.
            
            For each persona provide:
            - role
            - perspective
            
            Return ONLY valid JSON.
            
            Format:
            
            [
            {{
                "role": "Indian Macroeconomist",
                "perspective": "Focuses on GDP growth, demographics, and economic reforms."
            }},
            {{
                "role": "Chinese Industrial Policy Expert",
                "perspective": "Focuses on manufacturing, exports, and industrial policy."
            }}
            ]
            You must respond ONLY with raw, valid JSON. Do not include markdown formatting, backticks, or conversational text. Start your response directly with the JSON array. Ensure the JSON is properly formatted and can be parsed without errors.
            Requirements:
            - Roles must be professional expert roles, not specific real people.
            - Each role should represent a unique perspective.
            - Perspectives should be concise (1-2 sentences).
            - Do not include markdown.
            - Do not include explanations outside the JSON.
            """

        result = llm.invoke(prompt)

        return json.loads(result.content)