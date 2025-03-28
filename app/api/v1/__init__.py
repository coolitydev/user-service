from fastapi import APIRouter
from api.v1.user.router import router as user_router
from api.v1.wallet.router import router as wallet_rouer

router = APIRouter(prefix="/v1")
router.include_router(user_router)
router.include_router(wallet_rouer)
