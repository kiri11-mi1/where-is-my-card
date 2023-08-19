import logging

from aiogram import Bot, Dispatcher, executor, types

import settings

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] -  %(name)s - %(filename)s: %(lineno)d - %(message)s"    )

credentials = settings.Credentials()
bot = Bot(token=credentials.TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Hello World')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
