from sqlalchemy.ext.asyncio import AsyncSession
from Schemas.all_db_schemas import ProjectCreate
from backend.database.crud_agents import crud_project
from backend.core.dependencies import get_current_user
from backend.database.database_session import AsyncSessionLocal

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

