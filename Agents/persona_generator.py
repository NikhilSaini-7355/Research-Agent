from LLM.groq_client import llm
from Prompts.PersonaGeneratorPrompt import generate_persona_prompt
from Schemas.PersonaGeneratorSchema import ExpertRolesSchema
import json
import uuid
from backend.database.database_session import AsyncSessionLocal
from Schemas.all_db_schemas import PersonaCreate
from backend.database.crud_agents import crud_persona


class PersonaGenerator:

    async def generate_persona(self, topic_analysis, project_id):

        prompt = generate_persona_prompt(
            topic=topic_analysis.topic,
            domain=topic_analysis.domain,
            difficulty=topic_analysis.difficulty,
            subtopics=topic_analysis.subtopics,
            keywords=topic_analysis.keywords,
            research_goals=topic_analysis.research_goals
        )

        structured_llm = llm.with_structured_output(
            ExpertRolesSchema
        )

        personas = structured_llm.invoke(prompt)
        project_id = uuid.UUID(project_id)  # Convert project_id to UUID

        async with AsyncSessionLocal() as session:
            try:
                # Save each expert role to the database
                for expert in personas.experts:
                    persona_data = PersonaCreate(
                        project_id=project_id,
                        role=expert.role,
                        expertise=expert.expertise,
                        research_dimension=expert.research_dimension,
                        perspective=expert.perspective
                    )
                    persona = await crud_persona.create(db=session, obj_in=persona_data)
                    print(f"✅ Persona Generated: {persona.role}")
                
                # ─── THE CRUCIAL MISSING PIECE ──────────────────────────────────
                # Explicitly commit the transaction so changes persist in the DB
                await session.commit() 
                print("💾 All personas successfully committed to the database.")
                # ────────────────────────────────────────────────────────────────
            except Exception as e:
                import traceback
                traceback.print_exc()  # <--- Add this line to bypass CustomException masking
                print(f"\n❌ Persona Saving Failed: {e}")
                await session.rollback()
                raise e
                
        return personas