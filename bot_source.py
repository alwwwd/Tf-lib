from lib import update_status

from db import make_list
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
# from dotenv import load_dotenv
import sys
from aiogram.client.session.aiohttp import AiohttpSession
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


token = getenv("BOT_TOKEN")
bot = Bot(token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(mes: types.Message):
    print("hi")
    await mes.answer(f"🇷🇺Я бот на базt TF lib API версии 2.0! Я отслеживаю бет 24/7, и оповещаю о доступности\nДля активации бота воспользуйтесь командой /start_monitoring\n\n🇬🇧I am a bot based on TF lib API v 2.0! I monitor beta 24/7 and notify about availability. To activate the bot, use the command /start_monitoring.")
    # await mes.answer(update_status(mes,code_and_status))

@dp.message(Command("start_monitoring"))
async def start_monitoring(mes: types.Message):
    await mes.answer(f"Ожидайте, {mes.from_user.first_name}")
    print(f"{mes.from_user.first_name}")
    code_and_status =  make_list()
    # print(update_status(mes,code_and_status))
    background_tasks = set()
    task = asyncio.create_task(update_status(mes, code_and_status))
    background_tasks.add(task)

    # Ожидаем выполнения фоновой задачи
    await asyncio.wait({task})
    await mes.answer({task})

    # После завершения задачи удаляем ее из множества
    background_tasks.remove(task)

    


# @dp.message_handler(commands=["kill"])
# async def kill(mes: types.Message):
#    sys.exit() 
@dp.message(Command("add_beta"))
async def add_beta(mes: types.Message):
    await mes.answer(f"Заполните форму:\n\nhttps://forms.gle/qkx35CSc72LPZEZY9")
        
@dp.message(CommandObject("start_monitoring"))
async def start_monitoring(mes: types.Message):
    await mes.answer(f"Ожидайте, {mes.from_user.first_name}")
    print(f"{mes.from_user.first_name}")
    code_and_status =  make_list()
    # print(update_status(mes,code_and_status))
    background_tasks = set()
    task = asyncio.create_task(update_status(mes, code_and_status))
    background_tasks.add(task)

    # Ожидаем выполнения фоновой задачи
    await asyncio.wait({task})
    await mes.answer({task})

    # После завершения задачи удаляем ее из множества
    background_tasks.remove(task)
    
async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # session = AiohttpSession(proxy="http://proxy.server:3128")
    # bot = Bot(token, parse_mode=ParseMode.HTML,session=session)
    bot = Bot(token, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())