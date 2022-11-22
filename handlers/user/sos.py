
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.markups import all_right_message, cancel_message, submit_markup
from aiogram.types import Message
from states import SosState
from filters import IsUser
from loader import dp, db, bot


@dp.message_handler(text='❓ Savollar')
async def cmd_sos(message: Message):
    await SosState.question.set()
    await message.answer('Muammoning mohiyati nimada? Iloji boricha batafsil tasvirlab bering va administrator sizga albatta javob beradi.', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=SosState.question)
async def process_question(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text

    await message.answer("Hammasi to'g'ri ekanligiga ishonch hosil qiling.", reply_markup=submit_markup())
    await SosState.next()


@dp.message_handler(lambda message: message.text not in [cancel_message, all_right_message], state=SosState.submit)
async def process_price_invalid(message: Message):
    await message.answer("Bunday imkoniyat yo'q edi.")


@dp.message_handler(text=cancel_message, state=SosState.submit)
async def process_cancel(message: Message, state: FSMContext):
    await message.answer('Bekor qilindi!', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text=all_right_message, state=SosState.submit)
async def process_submit(message: Message, state: FSMContext):

    cid = message.chat.id

    if db.fetchone('SELECT * FROM questions WHERE cid=?', (cid,)) == None:

        async with state.proxy() as data:
            db.query('INSERT INTO questions VALUES (?, ?)',
                     (cid, data['question']))
        await bot.send_message(chat_id=452785654,text=f"Savol : {cid}, {data['question']})",)
        await message.answer('Yuborildi!', reply_markup=ReplyKeyboardRemove())

    else:

        await message.answer('Berilgan savollar sonining chegarasi oshib ketdi.', reply_markup=ReplyKeyboardRemove())

    await state.finish()
