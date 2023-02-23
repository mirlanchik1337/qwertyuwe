from aiogram import Bot, Dispatcher, types
from config import db, bot


from aiogram import Dispatcher, types
from config import bot

users = {}
async def python(massage: types.Message):
    user_name = massage.from_user.username
    if user_name:
        user_name = user_name
    else:
        user_name = massage.from_user.first_name
    if massage.from_user.username is not users:
        users[f'@{user_name}'] = massage.from_user.id
        print(users                 )

    else:
        pass


def reg_hand_extra(db: Dispatcher):
    db.register_message_handler(python)

