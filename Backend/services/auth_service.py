from Database.user_model import UserModel
from backend.core.security import (
    verify_password,
    create_access_token
)
from backend.database.crud_user import crud_user
from Database.user_model import UserModel
from fastapi import HTTPException, status
from backend.core.security import hash_password
from Schemas.all_db_schemas import UserCreate
from pydantic import EmailStr

class AuthService:

    def __init__(self, db):
        self.db = db

    async def get_user_by_email(self,email: EmailStr) -> UserModel | None:
        try:
            user = await crud_user.get_by_email(db=self.db, email=email)
            return user
        except Exception as e:
            logging.error(f"error during finding user by email :{str(e)}")

 
    async def login(self,email: EmailStr,password: str):
        user = await self.get_user_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "user": user,
            "access_token": token
        }



    async def get_user_by_id(self,user_id: str) -> UserModel | None:
        try:
            user = await crud_user.get(db=self.db, id=user_id)
            return user
        except Exception as e:
            logging.error(f"error during finding user by id :{str(e)}")

    async def register_user(
        self,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
    ):

        user = await self.get_user_by_email(email)

        if user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already registered with this email."
            )

        hashed_password = hash_password(password)

        new_user = UserCreate(
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=hashed_password,  # or hashed_password=... depending on your schema
        )

        return await crud_user.create(
            db=self.db,
            obj_in=new_user
        )
                
            
            