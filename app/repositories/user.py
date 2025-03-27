from typing import Optional
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User
from database.schemas.user import UserCreate


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
            self,
            user_data: UserCreate,
    ) -> Optional[User]:
        result = await self.session.execute(
            insert(User)
            .values(**user_data.model_dump())
            .returning(User)
        )
        return result.scalar_one_or_none()

    async def get_by_telegram_id(
            self,
            telegram_id: int
    ) -> Optional[User]:
        result = await self.session.execute(
            select(User)
            .where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()
