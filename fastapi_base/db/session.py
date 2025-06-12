from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.infrastructure.db.connection import async_session


async def get_session():
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()


SessionDep = Annotated[AsyncSession, Depends(get_session)]
