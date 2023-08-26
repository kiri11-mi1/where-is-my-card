from aiogram import Dispatcher, types
from services.database import BaseDatabaseService

from .replies import GREETING


async def start(message: types.Message, db_service: BaseDatabaseService) -> None:
    user = db_service.get_or_create_user(
        message.chat.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name,
    )
    await message.answer(GREETING.format(user.username))


def register_all_handlers(dp: Dispatcher, db_service: BaseDatabaseService) -> None:
    dp.register_message_handler(start, commands=['start'], db_service=db_service)
