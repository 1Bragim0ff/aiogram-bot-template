from aiogram import Dispatcher

from config import logger
from .admin import AdminFilter


async def register(dp: Dispatcher):
    filters = [AdminFilter]
    for fltr in filters:
        dp.filters_factory.bind(fltr)
    logger.info(f"Filters {list(map(lambda item: item.__name__, filters))} registered")
