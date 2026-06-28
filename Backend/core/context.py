from contextvars import ContextVar
from sqlalchemy.ext.asyncio import AsyncSession
from Database.user_model import UserModel
from uuid import UUID

# Create empty, secure global containers
db_session_var: ContextVar[AsyncSession] = ContextVar("db_session")
current_user_var: ContextVar[UserModel] = ContextVar("current_user")
current_project_id_var: ContextVar[UUID] = ContextVar("current_project_id")

# =====================================================================================================================
# Step 2: Set them at the very beginning of the request (FastAPI Middleware/Route)
# @app.post("/start")
# async def start_pipeline(db: AsyncSession = Depends(get_db), user: UserModel = Depends(get_user)):
#     # Inject the actual values into the containers
#     db_session_var.set(db)
#     current_user_var.set(user)
#     current_project_id_var.set(project_id)
#     # Call your deep function WITHOUT passing db or user
#     await deep_nested_function()


# Step 3: Retrieve them instantly, anywhere in your entire codebase
# # deeply_nested_file.py
# from backend.core.context import db_session_var, current_user_var, current_project_id_var

# async def deep_nested_function():
#     # Magically pull the exact DB and User for this specific request out of thin air
#     db = db_session_var.get()
#     user = current_user_var.get()
#     project_id = current_project_id_var.get()

#     print(f"Doing work for {user.email}")
#     await db.execute(...)