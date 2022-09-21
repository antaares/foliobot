from aiogram import types

from loader import dp, db
import asyncio



@dp.message_handler(text="Web-saytlar")
async def echo_web(message: types.Message):
    base_message = await message.answer("@daho_dasturchi tamonidan yaratilgan saytlar ro'yxati:\n")
    webs = db.get_webs()
    for web in webs:
        await asyncio.sleep(1)
        base_text = base_message.text
        n = "\n"
        if web[0] == 0:
            n = n*2
        base_message = await base_message.edit_text(base_text + f"{n}{web[0] + 1} |💠| {web[1]} - {web[2]}")
    await asyncio.sleep(1)
    await base_message.edit_text(base_message.text + "\n\nYurishda davom etamiz!")


# @dp.message_handler(text="Telegram bot")
# async def echo_robot(message: types.Message):
#     await message.answer("Telegram bot link")




@dp.message_handler(text="Telegram bot")
async def echo_robots(message: types.Message):
    base_message = await message.answer("@daho_dasturchi tamonidan yaratilgan botlar ro'yxati:\n")
    robots = db.get_robots()
    for robot in robots:
        await asyncio.sleep(1)
        base_text = base_message.text
        n = "\n"
        if robot[0] == 0:
            n = n*2
        base_message = await base_message.edit_text(base_text + f"{n}{robot[0] + 1} |💠| {robot[1]} - {robot[2]}")
    await asyncio.sleep(1)
    await base_message.edit_text(base_message.text + "\n\nYurishda davom etamiz!")





