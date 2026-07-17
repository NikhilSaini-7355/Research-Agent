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

import asyncio
async def main():
    async with AsyncSessionLocal() as db:
        current_user = "e687b70e-49ae-4542-87c2-eddab68a18ed"
        project_service = ProjectService(db=db)
        project = await project_service.create_project(
            user_id=current_user,
            topic="Large Language Models"
        )
        print(project.id)
        print(project.user_id)
        print(project.topic)

if(__name__ == "__main__"):
    asyncio.run(main())