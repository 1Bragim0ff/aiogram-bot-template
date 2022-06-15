import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

import config
import filters
import handlers
import middlewares
import utils


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    await middlewares.register(dp)
    await filters.register(dp)
    await utils.register(dp)
    await handlers.register(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
