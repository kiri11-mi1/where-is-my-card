from unittest import mock

import pytest
from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory
from services.database import User


class UserFactory(ModelFactory):
    __model__ = User


@pytest.fixture()
def fake_user() -> User:
    return UserFactory.build()


@pytest.fixture()
def mock_db_service(fake_user: User) -> mock.Mock:
    db_service = mock.Mock()
    db_service.get_or_create_user = mock.MagicMock(return_value=fake_user)
    return db_service


@pytest.fixture()
def mock_message_for_start(faker: Faker, fake_user: User) -> mock.Mock:
    message = mock.AsyncMock()
    message.text = faker.pystr()
    message.chat.id = fake_user.chat_id
    message.from_user.username = fake_user.username
    message.from_user.first_name = fake_user.first_name
    message.from_user.last_name = fake_user.last_name
    return message


@pytest.fixture()
def expected_response(fake_user: User) -> str:
    return (
        f'Приветсвую, {fake_user.username}! '
        'Чтобы получить QR-код, выбери программу лояльности, которую использует магазин.'
    )
