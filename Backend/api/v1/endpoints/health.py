from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {
        "status" : "healthy"
    }

