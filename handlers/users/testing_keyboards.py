from aiogram import types
from loader import dp
from keyboards.inline import first, row_keyboard, markup3, social
from keyboards.default import colors, phone

@dp.message_handler(commands="showbutton")
async def bot_echo(message: types.Message):
    await message.answer("Натисність на кнопку", reply_markup=first)

@dp.callback_query_handler(text="second")
async def second_step(call: types.CallbackQuery):
    await call.message.answer("Ви натиснули на кнопку")

@dp.message_handler(commands="choosecolor")
async def bot_color(message: types.Message):
    await message.answer("Виберіть один з кольорів", reply_markup=colors)

@dp.message_handler(commands="rowb")
async def bot_rowb(message: types.Message):
    await message.answer("Клавіатура row", reply_markup=row_keyboard)

@dp.message_handler(commands="markup3")
async def bot_markup3(message: types.Message):
    await message.answer("Клавіатура markup3", reply_markup=markup3)

@dp.message_handler(commands="contact")
async def bot_contact(message: types.Message):
    await message.answer("Клавіатура contact", reply_markup=phone)

@dp.message_handler(commands="social")
async def bot_social(message: types.Message):
    await message.answer("Клавіатура social", reply_markup=social)