import requests
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("COINGECKO_API_KEY is missing from the environment variables!")

base_url = os.getenv("BASE_URL")
db_url = os.getenv("DB_URL")
headers = {
    "x-cg-demo-api-key": api_key
}

params = {
    "vs_currency": "usd",
    "days": "30"
}

def fetch_candles(coin_id):
    url = f"{base_url}/coins/{coin_id}/ohlc"

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout as error:
        print(f"Connection Timeout: {error}")
        return None
    except requests.ConnectionError as error:
        print(f"Network error occurred: {error}")
        return None
    return data