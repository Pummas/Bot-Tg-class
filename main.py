from repository import *
from config import TOKEN
from bot import *

if __name__ == '__main__':
    rep = Repository(user="postgres", password="521E957er", host="127.0.0.1", port="5432", database="tg_bot2")
    bot = Bot(TOKEN, rep)
    bot.run()
