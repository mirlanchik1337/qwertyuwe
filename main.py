import logging
from aiogram import Bot, Dispatcher, executor, types
from config import db
from handler import client, admin, call_back, extra

client.reg_client(db)
call_back.reg_hand_callback(db)
admin.reg_ban(db)
extra.reg_hand_extra(db)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
