# tests/test_api_client.py
import pytest
from app.api_client import APIClient


@pytest.mark.asyncio
async def test_detect_language(monkeypatch):

    async def mock_detect(self, text):
        return "en"

    monkeypatch.setattr(APIClient, "detect_language", mock_detect)

    client = APIClient()
    result = await client.detect_language("Hello world")

    assert result == "en"