from aiogram import types
from utils.misc.throttling import rate_limit
from keyboards.constructors import InlineConstructor, CallType


@rate_limit(5)
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}!',
                     reply_markup=InlineConstructor.create(
                         [
                             [{'Тестовая кнопка': {CallType.URL: 'https://www.google.com/'}}]
                         ]
                     ))
