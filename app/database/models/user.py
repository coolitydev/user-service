from typing import Optional

from sqlalchemy import BIGINT, String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base, CreatedAtMixin, UpdatedAtMixin, uuid_pk


class User(Base, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "users"

    user_id: Mapped[uuid_pk]
    telegram_id: Mapped[int] = mapped_column(
        BIGINT,
        unique=True,
        nullable=False
    )
    username: Mapped[Optional[str]] = mapped_column(
        String(32),
        nullable=True
    )
    first_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False
    )
