from fastapi import FastAPI
from backend.api.v1.router import api_router

app = FastAPI(
    title="Research Agent API",
    version="1.0.0"
)

app.include_router(api_router)