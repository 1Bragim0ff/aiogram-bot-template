import logging
from os import environ

BOT_NAME = 'BOT_NAME'
BOT_TOKEN = environ.get(f'{BOT_NAME}_TOKEN')
ADMINS = []
ITEMS_ON_PAGE = 10

######### Logger
logger = logging.getLogger(BOT_NAME)
logging.basicConfig(
    level=logging.INFO,
    format=u'%(name)s:%(levelname)-0s | %(filename)s:%(lineno)d | %(message)s'
)

logger.debug(f"BOT_TOKEN: {BOT_TOKEN}")
logger.debug(f"ADMINS: {ADMINS}")
