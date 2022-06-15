from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from .start import bot_start


async def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
