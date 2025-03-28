from sqlalchemy import BIGINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base, UpdatedAtMixin, uuid_pk


class Wallet(Base, UpdatedAtMixin):
    __tablename__ = "wallets"

    wallet_id: Mapped[uuid_pk]
    telegram_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.telegram_id"),
        unique=True,
        nullable=False
    )
    balance: Mapped[int] = mapped_column(
        default=0,
        server_default="0",
        nullable=False
    )
