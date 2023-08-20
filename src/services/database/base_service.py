from typing import Protocol

from pydantic import UUID4

from .schemas import ProgramLoyalty, User


class BaseDatabaseService(Protocol):
    """Сервис базы данных."""

    def get_or_create_user(self, chat_id: str, username: str, first_name: str, last_name: str) -> User:
        """Получить или создать пользователя."""

    def get_program_loyalty(self, program_id: UUID4) -> ProgramLoyalty:
        """Получить программу лояльности"""

    def update_program_loyalty(self, program_id: UUID4, updated_data: dict) -> ProgramLoyalty:
        """Обновление программы лояльности"""

    def create_program_loyalty(self, created_data: dict) -> ProgramLoyalty:
        """Создание программы лояльности"""
