from typing import Any, Protocol

from pydantic import UUID4

from .schemas import ProgramLoyalty, User


class BaseDatabaseService(Protocol):
    """Базовый сервис базы данных."""

    def get_or_create_user(self, chat_id: str, username: str, first_name: str, last_name: str) -> User:
        """Получить или создать пользователя."""

    def get_program_loyalty(self, program_id: UUID4) -> ProgramLoyalty:
        """Получить программу лояльности"""

    def update_program_loyalty(self, program_id: UUID4, updated_data: dict[str, Any]) -> ProgramLoyalty:
        """Обновление программы лояльности"""

    def create_program_loyalty(self, created_data: dict[str, Any]) -> ProgramLoyalty:
        """Создание программы лояльности"""
