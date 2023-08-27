from typing import Protocol

from .schemas import User


class BaseDatabaseService(Protocol):
    """Базовый сервис базы данных."""

    def get_or_create_user(self, chat_id: str, username: str, first_name: str, last_name: str) -> User:
        """Получить или создать пользователя."""
