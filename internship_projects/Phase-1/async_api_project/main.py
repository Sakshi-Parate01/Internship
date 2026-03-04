# main.py
import asyncio
from app.sync_client import fetch_all_sync
from app.async_client import fetch_all_async
from app.utils import measure_time

@measure_time
def run_sync():
    return fetch_all_sync()

@measure_time
def run_async():
    return asyncio.run(fetch_all_async())

if __name__ == "__main__":
    print("=== Running Sync Version ===")
    sync_result = run_sync()
    print(sync_result)

    print("\n=== Running Async Version ===")
    async_result = run_async()
    print(async_result)