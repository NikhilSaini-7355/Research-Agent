from sqlalchemy.ext.asyncio import AsyncSession
from Schemas.all_db_schemas import ProjectCreate
from backend.database.crud_agents import crud_project, crud_article
from backend.core.dependencies import get_current_user
from backend.database.database_session import AsyncSessionLocal
import uuid

class ProjectService:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_project(self,user_id,topic,):

        project = ProjectCreate(
            user_id=user_id,
            topic=topic,
            status="CREATED",
        )

        return await crud_project.create(
            db=self.db,
            obj_in=project,
        )

    async def get_project_result(self, project_id):
        project_id = uuid.UUID(str(project_id))
        article = await crud_article.get_by_project(db=self.db, project_id=project_id)
        if article is None:
            return "No article present"
        return article.final_content

    async def get_projects_by_user_id(self, user_id):
        user_id = uuid.UUID(str(user_id))
        projects = await crud_project.get_by_user_id(db=self.db, user_id=user_id)
        return projects


