from aiogram.types import ReplyKeyboardMarkup as Rkm, KeyboardButton as Kb



keyboard_ = Rkm(
    keyboard=[
        [Kb(text="Statistiska"), Kb(text="Project qo'shish")],
        [Kb(text="Projectni o'chirish"),]
    ],
    resize_keyboard=True
)


add_project_menu = Rkm(
    keyboard=[
        [Kb(text="Robot"), Kb(text="web-sayt")],
    ],
    resize_keyboard=True
)