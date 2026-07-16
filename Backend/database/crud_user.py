from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database.crud_base import CRUDBase
from Database.user_model import UserModel
from Schemas.all_db_schemas import UserCreate, UserUpdate
from backend.core.security import hash_password,verify_password  # The hashing util we made earlier

class CRUDUser(CRUDBase[UserModel, UserCreate, UserUpdate]):
    
    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[UserModel]:
        """Fetch a user securely by their email for login routing."""
        query = select(self.model).where(self.model.email == email)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, *, obj_in: UserCreate) -> UserModel:
        """Overrides the base create to securely hash the password."""
        hashed_password = hash_password(obj_in.password)
        
        db_obj = UserModel(
            email=obj_in.email,
            firstname=obj_in.firstname,
            lastname=obj_in.lastname,
            hashed_password=hashed_password
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def authenticate(self, db: AsyncSession, *, email: str, password: str) -> Optional[UserModel]:
        """Validates login attempts."""
        user = await self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

crud_user = CRUDUser(UserModel)