from aiogram import Bot, Dispatcher, executor, types
import sqlite3 as sq
from aiogram.dispatcher.filters import Text
from keyboard import keyboard_start
import datetime

bot = Bot(token='7519860968:AAFEK9Xfx9vF67HCcQFy2WTHCohWnKyqrhA')
dp = Dispatcher(bot)


async def on_startup(_):
    global cur, base
    base = sq.connect('main.db')
    cur = base.cursor()
    if base:
        print('база подключена')
    base.execute('CREATE TABLE IF NOT EXISTS users(ID INTEGER, Callback INTEGER, Datatime REAL, Link TEXT,PRIMARY KEY("ID" AUTOINCREMENT))')

    base.commit()


async def start(message: types.Message):
    user = cur.execute(f"SELECT Callback FROM users WHERE Callback == '{message.chat.id}'").fetchone()
    if user is None:
        dates = datetime.date.today()
        cur.execute(f"INSERT INTO users(Datatime, Callback, Link) VALUES('{dates}','{message.chat.id}','{message.from_user.username}')")
        base.commit()
        await bot.send_message(message.chat.id, f"привет, {message.from_user.username}",reply_markup=keyboard_start)
    else:
        await bot.send_message(message.chat.id, f"привет, {message.from_user.username}", reply_markup=keyboard_start)
async def start_keyboard(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    print(callback.data)

    str = callback.data.split('_')[1]
    print(str)
    if str == "AI":
        await bot.send_message(callback.from_user.id, f"ИИ готов к работе (пока не работет)")
    if str == "Today":
        await bot.send_message(callback.from_user.id, f"Небезызвестный скользящий хакер")
    if str == "about":
        await bot.send_message(callback.from_user.id, f"Я будущий телеграмм бот оснащенный чат ГПТ")

if __name__ == '__main__':
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(start_keyboard,Text(startswith='start_'))
    executor.start_polling(dp,skip_updates=True, on_startup=on_startup)












