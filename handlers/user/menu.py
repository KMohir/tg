
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🍽Katalog'

cart = '🛒 Savat'
delivery_status = '🚚 Buyurtma holati'

settings = '⚙️Katalogni sozlash'
orders = '🚚 Buyurtmalar'
questions = '❓ Savollar'

@dp.message_handler(IsAdmin(), commands='start')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Menu', reply_markup=markup)

@dp.message_handler(IsUser(), commands='start')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(questions,catalog)
    markup.add(cart)

    await message.answer('Menu', reply_markup=markup)
