from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router

from database import db_helper
from database.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
