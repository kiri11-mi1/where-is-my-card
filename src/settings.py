from pydantic_settings import BaseSettings


class Credentials(BaseSettings):
    TELEGRAM_TOKEN: str
