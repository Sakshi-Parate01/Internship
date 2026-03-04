# app/async_client.py
import asyncio
import httpx
from app.config import TIMEOUT, MAX_CONCURRENT

URLS = {
    "cat": "https://catfact.ninja/fact",
    "dog": "https://dog.ceo/api/breeds/image/random",
    "crypto": "https://api.coindesk.com/v1/bpi/currentprice.json"
}

semaphore = asyncio.Semaphore(MAX_CONCURRENT)  # limit concurrent requests

async def fetch(client, name, url):
    """Async fetch with error handling, semaphore, and timeout"""
    async with semaphore:
        try:
            response = await client.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            return name, response.json()
        except httpx.RequestError as e:
            return name, {"error": f"Request failed: {e}"}
        except httpx.HTTPStatusError as e:
            return name, {"error": f"HTTP error: {e.response.status_code}"}

async def fetch_all_async():
    """Run all fetches concurrently using gather"""
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(fetch(client, name, url)) for name, url in URLS.items()]
        results = await asyncio.gather(*tasks)
    return {name: data for name, data in results}

# Example of cancellation (optional demo)
async def fetch_with_cancel():
    task = asyncio.create_task(fetch_all_async())
    await asyncio.sleep(1)  # wait a bit
    task.cancel()  # cancel the task
    try:
        await task
    except asyncio.CancelledError:
        print("Fetch task was cancelled")