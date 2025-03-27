from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from repositories import UserRepository
from services import UserService


def get_user_service(session: AsyncSession = Depends(db_helper.session_getter)) -> UserService:
    user_repo = UserRepository(session=session)
    return UserService(user_repo)