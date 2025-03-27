from typing import Optional

from database.models import User
from database.schemas.user import UserCreate
from repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create(
            self,
            user_data: UserCreate,
    ) -> Optional[User]:
        user = await self.user_repo.create(user_data=user_data)
        if user:
            await self.user_repo.session.commit()
        return user

    async def get_by_telegram_id(
            self,
            telegram_id: int
    ) -> Optional[User]:
        return await self.user_repo.get_by_telegram_id(telegram_id=telegram_id)
