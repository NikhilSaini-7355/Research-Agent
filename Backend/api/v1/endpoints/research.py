import asyncio

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.core.dependencies import get_db
from backend.models.request_models import ResearchRequest
from backend.models.response_models import ResearchResponse
from backend.services.research_service import ResearchService
from backend.tasks.research_task import run_research_job

router = APIRouter()


@router.post("/",response_model=ResearchResponse)
async def create_research_job(
    request: ResearchRequest,
    db: Session = Depends(get_db)
):

    service = ResearchService(db)

    job = service.create_job(request.topic)

    asyncio.create_task(
        run_research_job(
            job.job_id,
            request.topic
        )
    )

    return ResearchResponse(
        job_id=job.job_id,
        status=job.status
    )