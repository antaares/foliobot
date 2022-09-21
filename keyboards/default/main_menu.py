from aiogram.types import ReplyKeyboardMarkup as Rkm, KeyboardButton as Kb



keyboard = Rkm(
    keyboard=[
        [Kb(text="Telegram bot"), Kb(text="Web-saytlar")],
    ],
    resize_keyboard=True
)