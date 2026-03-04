# app/api_client.py
class APIClient:
    async def detect_language(self, text: str):
        # simple mock for all text
        return "en"