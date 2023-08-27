from aiogram import types

from services.database.base_service import BaseDatabaseService

from .replies import GREETING


async def start(db_service: BaseDatabaseService, message: types.Message) -> None:
    user = db_service.get_or_create_user(
        message.chat.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name,
    )
    await message.answer(GREETING.format(username=user.username))
