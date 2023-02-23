from aiogram import types , Dispatcher
from config import bot , db
from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton


@db.callback_query_handler(text='loh2')
async def quiz3(call: types.CallbackQuery):
    answer = [
        'повар спрашивает повара',
        'coffin dance',
        'дережабль, ага',
        'я футбольный мячик',

    ]
    ques = 'откуда мем?'
    photo = open('images/41meOBDVh8L._UXNaN_FMjpg_QL85_.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='это coffing dance ты угадал!',
        open_period=30)

@db.callback_query_handler(text='loh')
# перехватчик нажатия кнопки
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='loh2')
    markup.add(button)
    ques = 'кто это?'
    answer = [
        'Бетмен-рыцарь ночи',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'оптимус прайм последний прайм'
    ]
    photo = open('images/images.jfif', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='это бетмен ты угадал',
        open_period=30,
        reply_markup=markup
    )

def reg_hand_callback(db:Dispatcher):
    db.register_callback_query_handler(quiz2 , text='loh')
    db.register_callback_query_handler(quiz3 , text='loh2')