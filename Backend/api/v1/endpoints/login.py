from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.dependencies import get_db
from Database.user_model import UserModel
from backend.core.dependencies import get_current_user
from backend.database.database_session import AsyncSessionLocal
from backend.services.project_service import ProjectService
from backend.services.research_service import ResearchService

router = APIRouter()
@router.get("/me")
def me(
    current_user: UserModel = Depends(get_current_user)
):
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "name": current_user.firstname + " " + current_user.lastname
    }

@router.get("/projects")
async def projects(current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    async with AsyncSessionLocal() as neon_db:
        project_service = ProjectService(db=neon_db)
        projects = await project_service.get_projects_by_user_id(current_user.id)
        # add job id adding logic here

    service = ResearchService(db)
    projects_with_jobs =  []
    for project in projects:
        if hasattr(project, "to_dict"):
            project_dict = project.to_dict()
        elif hasattr(project, "__table__"):
            project_dict = {c.name: getattr(project, c.name) for c in project.__table__.columns}
        else:
            project_dict = dict(project) 
        # Retrieve corresponding job_id from SQLite by project_id
        job = service.get_job_by_project_id(str(project_dict["id"]))
        project_dict["job_id"] = job.job_id if job else None
        projects_with_jobs.append(project_dict)

    return projects_with_jobs
