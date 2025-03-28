from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from repositories import WalletRepository
from services import WalletService


def get_wallet_service(session: AsyncSession = Depends(db_helper.session_getter)) -> WalletService:
    wallet_repo = WalletRepository(session=session)
    return WalletService(wallet_repo=wallet_repo)
