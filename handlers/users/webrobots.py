from aiogram import types

from loader import dp, db
import asyncio


@dp.message_handler(text="Web-saytlar")
async def echo_web(message: types.Message):
    base_text = "@daho_dasturchi tamonidan yaratilgan web-saytlar ro'yxati:\n"
    base_message = await message.answer(base_text)
    webs = db.get_webs()
    for web in webs:
        await asyncio.sleep(1)
        base_text += f"\n{web[0] + 1} |💠| <a href='{web[2]}'>{web[1]}</a>"
        base_message = await base_message.edit_text(base_text)
    await asyncio.sleep(1)
    await base_message.edit_text(base_text + "\n\nYurishda davom etamiz!")





@dp.message_handler(text="Telegram bot")
async def echo_robots(message: types.Message):
    base_text = "@daho_dasturchi tamonidan yaratilgan botlar ro'yxati:\n"
    base_message = await message.answer(base_text)
    robots = db.get_robots()
    for robot in robots:
        await asyncio.sleep(1)
        base_text += f"\n{robot[0] + 1} |💠| <a href='{robot[2]}'>{robot[1]}</a>"
        base_message = await base_message.edit_text(base_text)
    await asyncio.sleep(1)
    await base_message.edit_text(base_text + "\n\nYurishda davom etamiz!")

