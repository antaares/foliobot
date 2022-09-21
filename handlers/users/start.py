from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.default.main_menu import keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer(
        "Bu bot JAHONGIR 🇺🇿 ISMOILOV 🇺🇿 (@daho_dasturchi) ning shaxsiy va jamoaviy ishlarini kuzatib borish uchun mo'ljallangan.",
        reply_markup=keyboard)
    db.add_user(message.from_user.id, message.from_user.full_name)
