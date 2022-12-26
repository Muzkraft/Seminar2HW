from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_new = ReplyKeyboardMarkup(resize_keyboard=True)
kb_stop = ReplyKeyboardMarkup(resize_keyboard=True)

btn_new_game = KeyboardButton(text='/new_game')
btn_stop_game = KeyboardButton(text='/stop_game')
btn_level = KeyboardButton(text='/set_level')
btn_help = KeyboardButton(text='/help')

kb_new.add(btn_new_game, btn_level, btn_help)
kb_stop.add(btn_stop_game, btn_help)