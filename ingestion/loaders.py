import psycopg2
from ingestion.coingecko_client import fetch_candles, db_url

def insert_candles(coin_id, data):
    conn = None
    cur = None
    records_count = 0
    try:
        #connect and open cursor
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

        #define the query
        insert_query = "INSERT INTO raw.coin_prices (coin_id, timestamp, open, high, low, close) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (coin_id, timestamp) DO NOTHING"

        # Loop and execute 
        for candle in data:
            row_data = (coin_id, *candle)
            cur.execute(insert_query, row_data)
            records_count += 1
        print(f"Successfully ingested {records_count} records of {coin_id}")

        # Commit changes permanently
        conn.commit()
        print("Data ingestion completed")

    except psycopg2.OperationalError as e:
        print(f"Operational Error: {e}")
        # Rollback changes if an error occurs
        if conn:
            conn.rollback()
    finally:
        # 7. Clean up and close resources
        if cur:
            cur.close()
        if conn:
            conn.close()