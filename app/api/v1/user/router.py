from typing import Annotated

from fastapi import APIRouter, Depends

from api.v1.user.dependencies import get_user_service
from database.schemas.user import UserRead, UserCreate
from services import UserService

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/", response_model=UserRead)
async def create_user(
        user_data: UserCreate,
        user_service: Annotated[UserService, Depends(get_user_service)],
):
    user = await user_service.create(user_data=user_data)
    return user


@router.get("/{telegram_id}", response_model=UserRead)
async def get_user(
        telegram_id: int,
        user_service: Annotated[UserService, Depends(get_user_service)]
):
    return await user_service.get_by_telegram_id(telegram_id=telegram_id)
