from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from config import logger


async def register(dp: Dispatcher):
    middlewares = [ThrottlingMiddleware]
    for middleware in middlewares:
        dp.middleware.setup(middleware())
    logger.info(f"Middlewares {list(map(lambda item: item.__name__, middlewares))} registered")
