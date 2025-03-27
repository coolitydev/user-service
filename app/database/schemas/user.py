from uuid import UUID

from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    telegram_id: int
    username: str
    first_name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    user_id: UUID
    created_at: datetime
