# app/sync_client.py
import requests
from app.config import TIMEOUT

URLS = {
    "cat": "https://catfact.ninja/fact",
    "dog": "https://dog.ceo/api/breeds/image/random",
    "crypto": "https://api.coindesk.com/v1/bpi/currentprice.json"
}

def fetch(url):
    """Fetch data synchronously with error handling"""
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_all_sync():
    results = {}
    for name, url in URLS.items():
        results[name] = fetch(url)
    return results