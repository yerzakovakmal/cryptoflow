CREATE SCHEMA raw;
CREATE SCHEMA marts;


DROP TABLE IF EXISTS raw.coin_metadata;
CREATE TABLE raw.coin_metadata(
    id VARCHAR(50) PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    name VARCHAR(100) NOT NULL,
    market_rank INTEGER
);

DROP TABLE IF EXISTS raw.coin_prices;

CREATE TABLE raw.coin_prices(
    coin_id VARCHAR(50) NOT NULL,
    timestamp BIGINT NOT NULL,
    open NUMERIC(20, 8),
    high NUMERIC(20, 8),
    low NUMERIC(20, 8),
    close NUMERIC(20, 8),

    PRIMARY KEY (coin_id, timestamp)
);