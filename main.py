from aiogram import types, Dispatcher, Bot, executor
from api import weather
from environs import Env

env = Env()
env.read_env()

token = env.str('token')

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Assalomu alaykum!Bot sizga shahringizdagi ob-havo haqida ma'lumot beradi!")


@dp.message_handler(content_types='text')
async def start_message(message: types.Message):
    text = message.text
    data = weather(text)
    if data == 'Error':
        await message.answer(f"Siz so'ragan ma'lumot topilmadi")
    else:
        await message.answer(f"Siz so'ragan ma'lumot\n"
                             f"{data}")


if __name__ == '__main__':
    executor.start_polling(dp)
