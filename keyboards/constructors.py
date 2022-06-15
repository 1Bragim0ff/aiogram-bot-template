from enum import Enum
from typing import Callable, Dict, List, Union

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import ITEMS_ON_PAGE
from .callbacks import TO_MAIN_MENU


class CallType(Enum):
    URL = 'URL'
    CALLBACK_DATA = 'CALLBACK_DATA'


class ScrollSide(Enum):
    NEXT = 'NEXT'
    PREVS = 'PREVS'
    IN_SITU = 'IN_SITU'


class DefaultConstructor:
    @staticmethod
    def create(
            schema: List[List[str]],
            resize_keyboard: bool = True,
            one_time_keyborad: bool = False
    ) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyborad
        )

        for actions in schema:
            buttons = []
            for action in actions:
                buttons.append(KeyboardButton(text=action))
            markup.add(*buttons)

        return markup


class InlineConstructor:

    @staticmethod
    def create(
            schema: List[List[Dict[str, Dict[CallType, Union[str, CallbackData]]]]],
            row_width: int = 3
    ) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=row_width)

        for actions in schema:
            buttons = []
            for action in actions:
                for key, data in action.items():
                    for type, payload in data.items():
                        if type == CallType.URL:
                            buttons.append(InlineKeyboardButton(
                                text=key, url=payload))
                        elif type == CallType.CALLBACK_DATA:
                            buttons.append(InlineKeyboardButton(
                                text=key, callback_data=payload))
            markup.add(*buttons)

        return markup


class ScrollInlineConstructor:

    @staticmethod
    def create(
            data: list,
            page: int,
            side: ScrollSide,
            callback: Callable,
            callbackScroll: Callable
    ) -> InlineKeyboardMarkup:
        if side == ScrollSide.NEXT:
            page += 1
        elif side == ScrollSide.PREVS:
            page -= 1
        elif side == ScrollSide.IN_SITU:
            pass

        nextPage = data[ITEMS_ON_PAGE * (page + 1) - ITEMS_ON_PAGE: ITEMS_ON_PAGE * (page + 1)]
        if len(nextPage) < 0:
            page -= 1

        data = data[ITEMS_ON_PAGE * page - ITEMS_ON_PAGE: ITEMS_ON_PAGE * page]

        return InlineConstructor.create([
            *[[callback(item, page)] for item in data],
            [
                {'<-': {CallType.CALLBACK_DATA: TO_MAIN_MENU if page == 1 else callbackScroll.new(side='PREVS', page=page)}},
                {page: {CallType.CALLBACK_DATA: 'page'}},
                {'->': {CallType.CALLBACK_DATA: callbackScroll.new(side='NEXT', page=page)}} if len(nextPage) > 0 else {}
            ],
            [
                {'<- На главную': {CallType.CALLBACK_DATA: TO_MAIN_MENU}} if page > 1 else {}
            ]
        ])
