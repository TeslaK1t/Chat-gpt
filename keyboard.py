from aiogram import types

def keyboard_start():
    start_keyboard = types.InlineKeyboardMarkup(row_width=2)
    start_b1 = types.InlineKeyboardButton(text="Про меня", callback_data="start_about")
    start_b2 = types.InlineKeyboardButton(text="Перейти к чату ГПТ", callback_data="start_AI")
    start_b3 = types.InlineKeyboardButton(text="Про моего создателя", callback_data="start_Today")
    start_keyboard.add(start_b1, start_b2, start_b3)
    return start_keyboard
keyboard_start = keyboard_start()

#check

#check1