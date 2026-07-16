from fastapi import FastAPI, APIRouter
from backend.api.v1.endpoints import health,research

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    health.router,
    tags=["Health"]
)

api_router.include_router(
    research.router,
    prefix="/research",
    tags=["Research"]
)