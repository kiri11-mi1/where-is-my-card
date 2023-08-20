from typing import Any

from pydantic import UUID4, BaseModel


class User(BaseModel):
    chat_id: str
    username: str
    first_name: str | None
    last_name: str | None


class ProgramLoyalty(BaseModel):
    id: UUID4
    user_id: str
    code: str
    slug: str
    credentials: dict[str, Any]  # TODO: схемы пайдантика
