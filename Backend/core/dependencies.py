from backend.database.database import SessionLocal
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.security import decode_access_token
from backend.services.auth_service import AuthService
from backend.database.database_session import get_db_neon
from Database.user_model import UserModel

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db_neon)
):

    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    auth_service = AuthService(db)

    user = await auth_service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user
