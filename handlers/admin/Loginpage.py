from data.config import ADMINS
from loader import dp, db 

from aiogram import types

from filters.is_admin import IsAdmin
from aiogram.dispatcher.storage import FSMContext
from states.admin_menu import AdminMenu

from keyboards.default.admin_menu import keyboard_, add_project_menu
from keyboards.default.main_menu import keyboard

@dp.message_handler(IsAdmin(),commands=['login'])
async def login_page(message: types.Message):
    await message.answer('Admin panelga hush kelibsiz!', reply_markup=keyboard_)

@dp.message_handler(commands='cancel', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await state.finish()
    await message.answer('Buyruq bekor qilindi!', reply_markup=keyboard)

@dp.message_handler(IsAdmin(),text='Statistiska')
async def statistics(message: types.Message):
    count = db.count()
    await message.answer(f"Jami userlar: {count}")



@dp.message_handler(IsAdmin(),text="Project qo'shish")
async def add_project(message: types.Message):
    await message.answer('Project turini tanlang:', reply_markup=add_project_menu)
    await AdminMenu.add_project.set()


@dp.message_handler(IsAdmin(),state=AdminMenu.add_project)
async def get_project_type(message: types.Message,state: FSMContext):
    if message.text == 'Robot':
        await message.answer('Robot nomini kiriting:')
        await AdminMenu.get_args.set()
        await state.update_data(type='robot')
    elif message.text == 'web-sayt':
        await message.answer('Web-sayt nomini kiriting:')
        await AdminMenu.get_args.set()
        await state.update_data(type='web-sayt')


@dp.message_handler(IsAdmin(),state=AdminMenu.get_args)
async def get_project_name(message: types.Message,state: FSMContext):
    data = await state.get_data()
    type = data.get('type')
    if type == 'robot':
        await message.answer('Robot linkini kiriting:')
        await AdminMenu.get_link.set()
        await state.update_data(name=message.text)
    elif type == 'web-sayt':
        await message.answer('Web-sayt linkini kiriting:')
        await AdminMenu.get_link.set()
        await state.update_data(name=message.text)



@dp.message_handler(IsAdmin(),state=AdminMenu.get_link)
async def get_project_link(message: types.Message,state: FSMContext):
    data = await state.get_data()
    type = data.get('type')
    name = data.get('name')
    if type == 'robot':
        db.add_robot(name=name,url=message.text)
        await message.answer('Project qo\'shildi!', reply_markup=keyboard_)
        await state.finish()
    elif type == 'web-sayt':
        db.add_web(name=name,url=message.text)
        await message.answer('Project qo\'shildi!', reply_markup=keyboard_)
        await state.finish()



@dp.message_handler(text="Projectni o'chirish")
async def delete_projects(message: types.Message):
    await message.answer("Project turini tanlang", reply_markup=add_project_menu)
    await AdminMenu.choice_delete.set()



@dp.message_handler(IsAdmin(), state=AdminMenu.choice_delete)
async def get_type(message: types.Message, state: FSMContext):
    if message.text == 'Robot':
        await message.answer('Robot idini kiriting:')
        await AdminMenu.get_id.set()
        await state.update_data(type='robot')
    elif message.text == 'web-sayt':
        await message.answer('Web-sayt idini kiriting:')
        await AdminMenu.get_id.set()
        await state.update_data(type='web-sayt')



@dp.message_handler(IsAdmin(), state=AdminMenu.get_id)
async def delete_project(message: types.Message, state: FSMContext):
    data = await state.get_data()
    type = data.get('type')
    id = message.text
    if type == 'robot':
        db.delete_robot(id = int(id))
        await message.answer('Project o\'chirildi!', reply_markup=keyboard_)
        await state.finish()
    elif type == 'web-sayt':
        db.delete_web(id=int(id))
        await message.answer('Project o\'ch irildi!', reply_markup=keyboard_)
        await state.finish()

