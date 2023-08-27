from services.database.base_service import BaseDatabaseService
from services.database.schemas import User


class PostgresService(BaseDatabaseService):
    def __init__(self, postgres_url: str) -> None:
        self._postgres_url = postgres_url

    def get_or_create_user(self, chat_id: str, username: str, first_name: str, last_name: str) -> User:
        return User(chat_id=chat_id, username=username, first_name=first_name, last_name=last_name)
