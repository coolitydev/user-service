from typing import Optional

from database.models import Wallet
from repositories import WalletRepository


class WalletService:
    def __init__(self, wallet_repo: WalletRepository):
        self.wallet_repo = wallet_repo

    async def create(
            self,
            telegram_id: int
    ) -> Optional[Wallet]:
        try:
            wallet = await self.wallet_repo.create(telegram_id=telegram_id)
            await self.wallet_repo.session.commit()
            return wallet
        except Exception as e:
            await self.wallet_repo.session.rollback()
            raise e

    async def get_by_telegram_id(
            self,
            telegram_id: int
    ) -> Optional[Wallet]:
        return await self.wallet_repo.get_by_telegram_id(telegram_id=telegram_id)
