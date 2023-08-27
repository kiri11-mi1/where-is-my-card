import logging
from functools import partial

from aiogram import Bot, Dispatcher, executor

import settings
from handlers import endpoints
from services.database.mongo_service import MongoService

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] -  %(name)s - %(filename)s: %(lineno)d - %(message)s")

# Создание зависимостей
credentials = settings.Credentials()
bot = Bot(token=credentials.TELEGRAM_TOKEN)
dp = Dispatcher(bot)
db_service = MongoService('sss')

# Регистрация хендлеров
dp.register_message_handler(partial(endpoints.start, db_service), commands=['start'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
