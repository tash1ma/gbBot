import logging
from aiogram import Router, types, F
from aiogram.filters.command import Command
from rndmFox import fox
from keyboards.keyboards import kb1, kb2


router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(text="Привет, я Габриетт.",reply_markup=kb2)



# Обработчик команды /info
@router.message(Command("info"))
async def send_info(message: types.Message):
    await message.answer("Это информационное сообщение о боте.")


# Обработчик команды /user
@router.message(Command("user"))
async def send_user_info(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Информация о пользователе:\nID: {user.id}\nИмя: {user.first_name}\nФамилия: {user.last_name or 'не указана'}\nUsername: @{user.username or 'не указан'}")


# Обработчик команды /help
@router.message(Command("help"))
async def send_help(message: types.Message):
    logging.info("Received /help command")
    help_text = """

Доступные команды:
/start - Начать работу с ботом
/info - Получить информацию о боте
/user - Получить информацию о пользователе
/help - Показать это сообщение
/fox - Показать случайную фотографию лисы
/prof - Выбрать питомца 
    """
    await message.answer(help_text)


@router.message(Command("fox"))
async def send_fox(message: types.Message):
    img_fox = fox()
    await message.answer("Вот ваша лиса:")
    await message.answer_photo(photo=img_fox)


# @router.message(F.text)
# async def handle_messages(message: types.Message):
#     msg_text = message.text.lower()
#     name = message.from_user.first_name
#     if any(greeting in msg_text for greeting in ["привет", "приветик"]):
#         await message.answer(f'Привет, {name}!')
#     elif 'пока' in msg_text:
#         await message.answer(f'Пока, {name}!')
#     elif 'ты кто' in msg_text:
#         await message.answer(f'Я бот Габриетт, приятно познакомиться, {name}!')
#     elif 'лиса' in msg_text or msg_text == 'покажи лису':
#         img_fox = fox()
#         await message.answer("Вот ваша лиса:")
#         await message.answer_photo(photo=img_fox)
#     else:
#         await message.answer(
#             f'Извините, {name}, я не понимаю вас. Попробуйте использовать команду /help для списка доступных команд.')