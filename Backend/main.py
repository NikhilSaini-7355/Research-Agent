from fastapi import FastAPI
from backend.api.v1.endpoints.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

from backend.api.v1.router import api_router

app = FastAPI(
    title="Research Agent API",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",  # Your React/Vite dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # Allows Authorization, Content-Type, etc.
)

app.include_router(api_router)
app.include_router(auth_router)