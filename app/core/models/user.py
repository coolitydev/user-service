import uuid
from typing import Optional

from sqlalchemy import text, BIGINT, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from core.models.base import Base, CreatedAtMixin, UpdatedAtMixin


class User(Base, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
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
