from uuid import UUID

from pydantic import BaseModel
from datetime import datetime


class WalletBase(BaseModel):
    pass


class WalletRead(WalletBase):
    wallet_id: UUID
    telegram_id: int
    balance: int
    updated_at: datetime
