import aiogram
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import datetime


class Bot:

    def __init__(self, token, repository):
        self.bot = aiogram.Bot(token=token)
        self.repository = repository

    def run(self):
        dp = Dispatcher(self.bot)
        dp.register_message_handler(self.process_start_command, commands=['start'])
        dp.register_message_handler(self.process_help_command, commands=['help'])
        dp.register_message_handler(self.process_menu_command, commands=['menu'])
        dp.register_message_handler(self.echo_message)

        executor.start_polling(dp)

    # @dp.message_handler(commands=['start'])
    async def process_start_command(self, message: types.Message):

        is_exist = self.repository.check_registration(message.from_user.id)
        if is_exist:
            await message.reply("Привет!")
        else:
            await message.reply("Как я могу к вам обращаться?")

    # @dp.message_handler(commands=['help'])
    async def process_help_command(self, message: types.Message):
        await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

    # @dp.message_handler(commands=['menu'])
    async def process_menu_command(self, message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Джун", "Мидл", "Синьор"]
        keyboard.add(*buttons)
        # self.keyboard = keyboard
        await message.answer("Каков твой уровень?", reply_markup=keyboard)

    # @dp.message_handler(lambda message: message.text == "Джун")
    # async def junior(message: types.Message):
    #     self.repository.return_name_skill(message.from_user.id)

    # @dp.message_handler()
    async def echo_message(self, msg: types.Message):
        print(msg)
        try:
            self.repository.check_registration(msg.from_user.id)
            await self.bot.send_message(msg.from_user.id, "Для того, чтобы вызвать меню наберите команду /menu")
            self.repository.save_message(msg.from_user.id, msg.text, datetime.datetime.now())
        except:
            self.repository.register_user(msg.from_user.id, msg.text)
            a = "Привет, {name}".format(name=msg.text)
            await self.bot.send_message(msg.from_user.id, a)
