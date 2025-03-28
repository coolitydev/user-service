from typing import Annotated

from fastapi import APIRouter, Depends

from api.v1.wallet.dependencies import get_wallet_service

from database.schemas.wallet import WalletRead
from services.wallet import WalletService

router = APIRouter(
    prefix="/wallet",
    tags=["Wallet"]
)


@router.post("/create/{telegram_id}", response_model=WalletRead)
async def create_wallet(
        telegram_id: int,
        wallet_service: Annotated[WalletService, Depends(get_wallet_service)],
):
    return await wallet_service.create(telegram_id=telegram_id)


@router.get("/get/{telegram_id}")
async def get_wallet(
        telegram_id: int,
        wallet_service: Annotated[WalletService, Depends(get_wallet_service)]
):
    return await wallet_service.get_by_telegram_id(telegram_id=telegram_id)
