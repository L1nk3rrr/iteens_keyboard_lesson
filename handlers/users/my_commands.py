from aiogram import types

from loader import dp

@dp.message_handler(commands=['info'])
async def bot_say_info(message: types.Message):
    await message.answer(f"{message.from_user.full_name} - your language {message.from_user.language_code}")


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def bot_send_sticker(message: types.Message):
    await message.answer(f"Info about sticker\n animation - {message.sticker.is_animated}\n size - {message.sticker.file_size}")
    await message.answer_sticker(f"{message.sticker.file_id}")