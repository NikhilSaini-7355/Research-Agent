from LLM.groq_client import llm
from Prompts.question_generator_prompt import generate_questions_prompt
from Schemas.question_generator_schema import QuestionSchema
import json
import uuid
from Schemas.all_db_schemas import QuestionCreate
from backend.database.crud_agents import crud_question
from backend.database.database_session import AsyncSessionLocal

class question_generator_agent:
    def generate_questions(self,topic,expert):
        prompt = generate_questions_prompt(
            topic = topic,
            role = expert.role,
            expertise = expert.expertise,
            research_dimension = expert.research_dimension,
            perspective = expert.perspective
        )
        structured_llm = llm.with_structured_output(QuestionSchema)
        result = structured_llm.invoke(prompt)
        return result

    async def save_queries(self, search_queries, project_id):
        project_id = uuid.UUID(project_id)
        async with AsyncSessionLocal() as session:
            try:
                question_data = QuestionCreate(
                    project_id=project_id,
                    queries=search_queries
                )
                question = await crud_question.create(db=session, obj_in=question_data)
                await session.commit() 
                print("💾 All questions successfully committed to the database.")

            except Exception as e:
                import traceback
                traceback.print_exc()  # <--- Add this line to bypass CustomException masking
                print(f"\n❌ Question Saving Failed: {e}")
                await session.rollback()
                raise e




