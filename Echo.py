import asyncio
import logging

from environs import Env
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

env = Env()
env.read_env('.env')

bot = Bot(env('BOT_SECRET'))
dp = Dispatcher()


@dp.message()
async def any_message(message: types.Message):
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
