from pydantic_settings import BaseSettings


class Credentials(BaseSettings):
    TELEGRAM_TOKEN: str
    DB_URL: str  # TODO: добавить в .dockerenv
    DB_PASSWORD: str  # TODO: добавить в .dockerenv
    DB_USER: str  # TODO: добавить в .dockerenv
