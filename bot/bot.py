import aiogram
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# from aiogram.types import ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup, KeyboardButton, \
#     InlineKeyboardMarkup, InlineKeyboardButton
import datetime


class Bot:

    def __init__(self, token, repository):
        self.bot = aiogram.Bot(token=token)
        self.repository = repository

    def run(self):
        dp = Dispatcher(self.bot)

        @dp.message_handler(commands=['start'])
        async def process_start_command(message: types.Message):
            try:
                self.repository.check_registration(message.from_user.id)
                await message.reply("Привет!")
            except:
                await message.reply("Как я могу к вам обращаться?")

        @dp.message_handler(commands=['help'])
        async def process_help_command(message: types.Message):
            await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

        @dp.message_handler()
        async def echo_message(msg: types.Message):
            try:
                self.repository.check_registration(msg.from_user.id)
                await self.bot.send_message(msg.from_user.id, msg.text)
                self.repository.save_message(msg.from_user.id, msg.text, datetime.datetime.now())
            except:
                self.repository.register_user(msg.from_user.id, msg.text)
                a = "Привет, " + msg.text
                await self.bot.send_message(msg.from_user.id, a)

        executor.start_polling(dp)
