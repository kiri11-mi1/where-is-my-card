from unittest import mock

import pytest
from handlers import start


@pytest.mark.asyncio()
async def test_start_endpoint(
    mock_db_service: mock.Mock,
    mock_message_for_start: mock.Mock,
    expected_response: str,
) -> None:
    await start(mock_db_service, mock_message_for_start)
    mock_message_for_start.answer.assert_called_with(expected_response)
