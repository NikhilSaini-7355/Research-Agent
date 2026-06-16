from uuid import UUID
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.crud_base import CRUDBase

from Database.extracted_content_model import ExtractedContentModel
from Database.question_generator_model import ResearchQuestionModel
from Database.persona_model import ResearchPersonaModel
from Database.generated_article_model import GeneratedArticleModel
from Database.project_model import ProjectModel

from Schemas.all_db_schemas import (
    PersonaCreate, PersonaUpdate,
    QuestionCreate, QuestionUpdate,
    ExtractedContentCreate, ExtractedContentUpdate,
    ArticleCreate, ArticleUpdate,
    ProjectCreate, ProjectUpdate
)

# --- PERSONA CRUD ---
class CRUDPersona(CRUDBase[ResearchPersonaModel, PersonaCreate, PersonaUpdate]):
    async def get_by_project(self, db: AsyncSession, *, project_id: UUID) -> List[ResearchPersonaModel]:
        query = select(self.model).where(self.model.project_id == project_id)
        result = await db.execute(query)
        return list(result.scalars().all())

# --- QUESTION CRUD ---
class CRUDQuestion(CRUDBase[ResearchQuestionModel, QuestionCreate, QuestionUpdate]):
    async def get_by_persona(self, db: AsyncSession, *, persona_id: UUID) -> List[ResearchQuestionModel]:
        query = select(self.model).where(self.model.persona_id == persona_id)
        result = await db.execute(query)
        return list(result.scalars().all())

# --- PROJECT CRUD ---
class CRUDProject(CRUDBase[ProjectModel, ProjectCreate, ProjectUpdate]):
    async def get_by_user_id(self, db: AsyncSession, *, user_id: UUID) -> List[ProjectModel]:
        """Fetch all research projects belonging to a specific user for their dashboard."""
        query = select(self.model).where(self.model.user_id == user_id).order_by(self.model.created_at.desc())
        result = await db.execute(query)
        return list(result.scalars().all())
        
    async def update_status(self, db: AsyncSession, *, project_id: UUID, new_status: str) -> Optional[ProjectModel]:
        """Quickly update the workflow status of a project (e.g., searching -> writing)."""
        project = await self.get(db=db, id=project_id)
        if project:
            project.status = new_status
            db.add(project)
            await db.commit()
            await db.refresh(project)
        return project

        
# --- EXTRACTED CONTENT CRUD ---
class CRUDExtractedContent(CRUDBase[ExtractedContentModel, ExtractedContentCreate, ExtractedContentUpdate]):
    async def get_pending_embeddings(self, db: AsyncSession, *, project_id: UUID) -> List[ExtractedContentModel]:
        """Used by your background worker to find text that needs to be sent to ChromaDB."""
        query = select(self.model).where(
            self.model.project_id == project_id,
            self.model.embedding_status == 'pending'
        )
        result = await db.execute(query)
        return list(result.scalars().all())

# --- GENERATED ARTICLE CRUD ---
class CRUDArticle(CRUDBase[GeneratedArticleModel, ArticleCreate, ArticleUpdate]):
    async def get_by_project(self, db: AsyncSession, *, project_id: UUID) -> Optional[GeneratedArticleModel]:
        query = select(self.model).where(self.model.project_id == project_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()

# Instantiate the helpers
crud_persona = CRUDPersona(ResearchPersonaModel)
crud_question = CRUDQuestion(ResearchQuestionModel)
crud_content = CRUDExtractedContent(ExtractedContentModel)
crud_article = CRUDArticle(GeneratedArticleModel)
crud_project = CRUDProject(ProjectModel)