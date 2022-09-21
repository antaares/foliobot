from aiogram.dispatcher.filters.state import StatesGroup, State




class AdminMenu(StatesGroup):
    is_admin = State()
    add_project = State()
    choice = State()
    get_args = State()
    get_link = State()
    choice_delete = State()
    get_id = State()