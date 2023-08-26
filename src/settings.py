from pydantic_settings import BaseSettings


class Credentials(BaseSettings):
    TELEGRAM_TOKEN: str
    DB_URL: str
    DB_PASSWORD: str
    DB_USER: str
