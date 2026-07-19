from backend.database.database_session import AsyncSessionLocal
from backend.services.auth_service import AuthService

import asyncio

async def work():
    async with AsyncSessionLocal() as session:
        try:
            service = AuthService(session)
            result = await service.login(
                email="hello@gmail.com",
                password="pass"
            )
            print(result["access_token"])
            print(result["user"].email)
        except Exception as e:
            raise e
            await session.rollback()

asyncio.run(work())