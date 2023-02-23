from aiogram import types, Dispatcher
from config import bot, ADMIN


async def ban(massage: types.Message):
    if massage.chat.type != 'private':
        if massage.from_user.id in ADMIN:
            await bot.kick_chat_member(massage.chat.id,
                                       massage.reply_-to_message.from_user.id)
            await massage.answer(f"он вышел сам")
        elif not massage.reply_to_message:
            await massage.answer(f'покажи кого банить мой хозяин ?')
        else:
            await massage.answer(f"ты не мой хозяин ")

            await massage.answer(f'@{massage.from_user.username} '
                                 f'{massage.reply_to_message.from_user.full_name}')
    else:
        await massage.answer(f"это не является группой ")

def reg_ban(db: Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
