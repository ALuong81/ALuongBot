import pandas as pd

def market_regime(index_df):
    if index_df is None or len(index_df) < 50:
        return "UNKNOWN"

    ma50 = index_df["close"].rolling(50).mean().iloc[-1]
    price = index_df["close"].iloc[-1]

    if price > ma50:
        return "BULL"
    else:
        return "BEAR"
