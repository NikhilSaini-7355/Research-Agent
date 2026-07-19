from fastapi import APIRouter, Depends

from backend.database.database_session import get_db_neon
from backend.models.request_models import LoginRequest,SignupRequest
from backend.models.response_models import LoginResponse,SignupResponse
from backend.services.auth_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login",response_model=LoginResponse)
async def login(
    request: LoginRequest,
    db: AsyncSession = Depends(get_db_neon)
):

    auth_service = AuthService(db)
    print( "hello" ,request)
    result = await auth_service.login(
        email=request.email,
        password=request.password
    )

    return LoginResponse(
        access_token=result["access_token"]
    )

@router.post("/signup",response_model=SignupResponse)
async def signup(
    request: SignupRequest,
    db: AsyncSession = Depends(get_db_neon)
):
    auth_service = AuthService(db)
    result = await auth_service.register_user(
        email=request.email,
        firstname=request.firstname,
        lastname=request.lastname,
        password=request.password
    )
    return SignupResponse(
        message = "Signed in successfully."
    )