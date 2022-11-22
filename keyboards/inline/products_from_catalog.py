from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx='', price=0):

    global product_cb

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f"Savatchaga qo'shish - {price}som", callback_data=product_cb.new(id=idx, action='add')))

    return markup