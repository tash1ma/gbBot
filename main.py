import logging
import asyncio
# from aiogram import Router, types
from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.filters import Command
# from rndmFox import fox
import config
import common, animalChoice
# from animalChoice import router as animal_router

async def main():
    API_TOKEN = config.token
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.include_router(common.router)
    dp.include_router(animalChoice.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
