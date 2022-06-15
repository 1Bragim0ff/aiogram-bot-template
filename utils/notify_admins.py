import logging

from aiogram import Dispatcher
import config


async def on_startup_notify(dp: Dispatcher):
    for admin in config.ADMINS:
        try:
            await dp.bot.send_message(admin, 'Бот запущен!')
        except Exception as err:
            logging.exception(err)
