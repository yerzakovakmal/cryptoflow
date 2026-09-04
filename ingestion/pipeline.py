from ingestion.coingecko_client import fetch_candles
from ingestion.loaders import insert_candles

def run_pipeline(coin_id):
    result = fetch_candles(coin_id=coin_id)
    print(result)

    if result is None:
        print(f"Skipping insert for {coin_id}")
        return
    insert_candles(coin_id=coin_id, data=result)

if __name__ == "__main__":
    run_pipeline("bitcoin")
    run_pipeline("ethereum")