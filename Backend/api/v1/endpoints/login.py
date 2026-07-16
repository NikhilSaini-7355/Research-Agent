from fastapi import APIRouter, Depends
from Database.user_model import UserModel
from backend.core.dependencies import get_current_user

router = APIRouter()
@router.get("/me")
def me(
    current_user: UserModel = Depends(get_current_user)
):
    return {
        "id": str(current_user.id),
        "email": current_user.email
    }