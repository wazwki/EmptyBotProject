import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

load_dotenv()
os.getenv("")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TOKEN"))

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Hello world")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
