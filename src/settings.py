from pydantic_settings import BaseSettings


class Credentials(BaseSettings):
    TELEGRAM_TOKEN: str


class MongoDB(BaseSettings):
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str

    ME_CONFIG_MONGODB_ADMINUSERNAME: str
    ME_CONFIG_MONGODB_ADMINPASSWORD: str
    ME_CONFIG_MONGODB_URL: str
