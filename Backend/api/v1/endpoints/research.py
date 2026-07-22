import asyncio

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Database.user_model import UserModel
from backend.core.dependencies import get_db
from backend.database.database_session import AsyncSessionLocal
from backend.models.request_models import ResearchRequest
from backend.models.response_models import ResearchResponse,ResearchStatusResponse
from backend.services.research_service import ResearchService
from backend.services.project_service import ProjectService
from backend.tasks.research_task import run_research_job
from backend.core.dependencies import get_current_user
router = APIRouter()

@router.post("/",response_model=ResearchResponse)
async def create_research_job(
    request: ResearchRequest,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):

    service = ResearchService(db)
    async with AsyncSessionLocal() as db:
        project_service = ProjectService(db=db)
        project = await project_service.create_project(
            user_id=current_user.id,
            topic=request.topic
        )
        print("Created Project ID:", project.id)


    job = service.create_job(topic=request.topic,user_id=current_user.id,project_id=project.id)
    print("Job ID:", job.job_id)
    asyncio.create_task(
        run_research_job(
            job.job_id
        )
    )

    return ResearchResponse(
        job_id=job.job_id,
        project_id=str(project.id),
        status=job.status
    )

@router.get("/{job_id}/status",response_model=ResearchStatusResponse)
def get_job_status(
    job_id: str,
    db: Session = Depends(get_db),
):
    service = ResearchService(db)

    job = service.get_job_status(job_id)

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research job not found."
        )

    return ResearchStatusResponse(
        job_id=job.job_id,
        status=job.status,
        progress=job.progress,
    )
    
@router.get("/{job_id}/result")
async def get_research_result(
    job_id: str,
    db: Session = Depends(get_db),
):
    research_service = ResearchService(db)

    job = research_service.get_result(job_id)

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research job not found."
        )

    async with AsyncSessionLocal() as neon_db:
        project_service = ProjectService(db=neon_db)
        final_content = await project_service.get_project_result(project_id=job.project_id)
    
    return {
        "final_markdown": final_content
    }