import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from database.models.base import Base, UpdatedAtMixin, uuid_pk


class Wallet(Base, UpdatedAtMixin):
    __tablename__ = "wallets"

    wallet_id: Mapped[uuid_pk]
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id"),
        unique=True,
        nullable=False
    )
    balance: Mapped[int] = mapped_column(
        default=0,
        server_default="0",
        nullable=False
    )

