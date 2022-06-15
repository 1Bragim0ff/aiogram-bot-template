from . import misc
from aiogram import Dispatcher
from .notify_admins import on_startup_notify
from .set_bot_commands import set_default_commands
from config import logger


async def register(dp: Dispatcher):
    await set_default_commands(dp)
    await on_startup_notify(dp)
    logger.info("Utils registered")
