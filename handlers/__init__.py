from aiogram import Dispatcher

import handlers.errors
import handlers.users
from config import logger


async def register(dp: Dispatcher):
    await errors.register(dp)
    await users.register(dp)
    logger.info("Handlers registered")
