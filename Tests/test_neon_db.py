import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os


# Import all your schemas
from Schemas.all_db_schemas import (
    UserCreate, ProjectCreate, PersonaCreate, 
    QuestionCreate, ExtractedContentCreate, ArticleCreate
)

# Import all your CRUD helpers
from backend.database.crud_user import crud_user
from backend.database.crud_agents import (
    crud_persona, crud_question, crud_content, crud_article, crud_project
)

load_dotenv()

# Replace with your actual Neon Database URL
DATABASE_URL = os.getenv("NEON_DATABASE_URL")

async def test_entire_multi_agent_pipeline():
    print("🚀 Initializing Database Connection...")
    engine = create_async_engine(DATABASE_URL, echo=False)
    AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

    async with AsyncSessionLocal() as session:
        try:
            # ==========================================
            # STAGE 1: AUTHENTICATION & INITIALIZATION
            # ==========================================
            print("\n--- 🧪 STAGE 1: Auth & Project Init ---")
            
            user_data = UserCreate(
                email="system_tester@neon.tech",
                firstname="System",
                lastname="Tester",
                password="secure_password"
            )
            user = await crud_user.create(db=session, obj_in=user_data)
            print(f"✅ User Created: {user.email} (ID: {user.id})")

            project_data = ProjectCreate(
                user_id=user.id,
                topic="The Future of Solid State Batteries",
                status="analyzing"
            )
            project = await crud_project.create(db=session, obj_in=project_data)
            print(f"✅ Project Created: {project.topic}")

            # ==========================================
            # STAGE 2: PERSONA & QUESTION GENERATION
            # ==========================================
            print("\n--- 🧪 STAGE 2: Multi-Agent Generation ---")
            
            persona_data = PersonaCreate(
                project_id=project.id,
                role="Material Scientist",
                expertise="Battery chemistry and energy density",
                research_dimension="Technical Feasibility",
                perspective="Academic and analytical"
            )
            persona = await crud_persona.create(db=session, obj_in=persona_data)
            print(f"✅ Persona Generated: {persona.role}")

            question_data = QuestionCreate(
                project_id=project.id,
                queries=["solid state electrolyte degradation", "dendrite formation solid state batteries"]
            )
            question = await crud_question.create(db=session, obj_in=question_data)
            print(f"✅ Questions Generated: {len(question.queries)} search queries queued.")

            # ==========================================
            # STAGE 3: SCRAPING & RAG PIPELINE
            # ==========================================
            print("\n--- 🧪 STAGE 3: Scraping & Extraction ---")
            
            content_data = ExtractedContentCreate(
                project_id=project.id,
                url="https://example.com/battery-research",
                title="Recent Advances in Solid State Tech",
                raw_content="Solid state batteries replace the liquid electrolyte with a solid compound..."
            )
            content = await crud_content.create(db=session, obj_in=content_data)
            print(f"✅ Content Extracted: Staged for ChromaDB embedding.")

            # ==========================================
            # STAGE 4: FINAL SYNTHESIS
            # ==========================================
            print("\n--- 🧪 STAGE 4: Final Article Generation ---")
            
            article_data = ArticleCreate(
                project_id=project.id,
                outline={"intro": "The Battery Revolution", "body": "Technical Challenges"}
            )
            article = await crud_article.create(db=session, obj_in=article_data)
            
            # Simulate the writer agent updating the draft
            updated_article = await crud_article.update(
                db=session,
                db_obj=article,
                obj_in={"final_content": "# The Future of Batteries\n\nThey are very efficient.", "confidence_score": 98.5}
            )
            print(f"✅ Article Written & Scored: {updated_article.confidence_score}/100")

            # ==========================================
            # STAGE 5: READ VERIFICATION
            # ==========================================
            print("\n--- 🧪 STAGE 5: Verification ---")
            fetched_personas = await crud_persona.get_by_project(db=session, project_id=project.id)
            print(f"✅ Verified: Found {len(fetched_personas)} personas linked to the project.")

        except Exception as e:
            print(f"\n❌ Pipeline Test Failed: {e}")
            await session.rollback()
        # finally:
            # ==========================================
            # STAGE 6: THE CASCADE CLEANUP TEST
            # ==========================================
            # print("\n🧹 Cleaning up database...")
            # if 'user' in locals():
            #     # By deleting the user, Postgres should cascade and delete the Project, 
            #     # Persona, Question, Content, and Article automatically!
            #     await crud_user.remove(db=session, id=user.id)
            #     print("✅ Test data completely wiped via Cascade Delete.")

    await engine.dispose()
    print("🛑 Disconnected.")

if __name__ == "__main__":
    asyncio.run(test_entire_multi_agent_pipeline())