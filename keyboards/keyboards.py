from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/info')
button3 = types.KeyboardButton(text='/fox')
button4 = types.KeyboardButton(text='/user')
button5 = types.KeyboardButton(text='/help')
button6 = types.KeyboardButton(text='/prof')

keyboard1 = [[button1, button2, button3],
            [button1, button2, button3]]
keyboard2 = [[button4, button5, button6],[button1, button2, button3]]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)