from aiogram import Bot, Dispatcher, types
from config import db, bot


async def echo(massage: types.Message):
    bad_word = ['java', 'front', 'javascript', 'ix', 'php', 'html', 'дурак', 'болван']
    username = f'@{massage.from_user.username}' \
               f'' if massage.from_user.username is not None else \
        massage.from_user.first_name

    for word in bad_word:
        if word in massage.text.lower().replace(" ", ""):
            await bot.delete_message(massage.chat.id, massage.message_id)
            await massage.answer(f'не матерись @{massage.from_user.username}')

    if massage.text.startswith("."):
        await bot.pin_chat_message(massage.chat.id, massage.message_id)
    if massage.text == "python":
        a = await bot.send_dice(massage.chat.id)
        print(a)



def reg_hand_extra(db: Dispatcher):
    db.register_message_handler(echo)
