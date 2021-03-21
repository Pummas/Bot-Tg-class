import aiogram
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime


class Bot:

    def __init__(self, token, repository):
        self.bot = aiogram.Bot(token=token)
        self.repository = repository

    def run(self):
        dp = Dispatcher(self.bot)

        @dp.message_handler(commands=['start'])
        async def process_start_command(message: types.Message):
            await message.reply("Привет!\nНапиши мне что-нибудь!")

        @dp.message_handler(commands=['help'])
        async def process_help_command(message: types.Message):
            await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

        @dp.message_handler()
        async def echo_message(msg: types.Message):
            await self.bot.send_message(msg.from_user.id, msg.text)
            self.repository.save_message(msg.from_user.id, msg.text, datetime.datetime.now())

        executor.start_polling(dp)
