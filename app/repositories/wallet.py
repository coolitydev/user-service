from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Wallet


class WalletRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
            self,
            telegram_id: int
    ) -> Optional[Wallet]:
        result = await self.session.execute(
            insert(Wallet)
            .values(telegram_id=telegram_id)
            .returning(Wallet)
        )
        return result.scalar_one_or_none()

    async def get_by_telegram_id(
            self,
            telegram_id: int
    ) -> Optional[Wallet]:
        result = await self.session.execute(
            select(Wallet)
            .where(Wallet.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()
