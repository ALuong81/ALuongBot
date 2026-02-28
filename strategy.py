import pandas as pd
from data import get_price

def calculate_rs(stock_df, index_df):
    if len(stock_df) < 60 or len(index_df) < 60:
        return 0

    stock_return = stock_df["close"].iloc[-1] / stock_df["close"].iloc[-60]
    index_return = index_df["close"].iloc[-1] / index_df["close"].iloc[-60]

    if index_return == 0:
        return 0

    return stock_return / index_return


def filter_stocks(symbol, stock_df, index_df):
    if stock_df is None or len(stock_df) < 200:
        return False, 0

    df = stock_df.copy()

    df["ma50"] = df["close"].rolling(50).mean()
    df["ma200"] = df["close"].rolling(200).mean()
    df["vol_avg20"] = df["volume"].rolling(20).mean()
    df["high60"] = df["high"].rolling(60).max()

    latest = df.iloc[-1]

    cond_trend = latest["close"] > latest["ma50"] and latest["ma50"] > latest["ma200"]
    cond_breakout = latest["close"] >= latest["high60"]
    cond_volume = latest["volume"] > 1.5 * latest["vol_avg20"]

    rs = calculate_rs(stock_df, index_df)
    cond_rs = rs > 1.1

    if cond_trend and cond_breakout and cond_volume and cond_rs:
        return True, round(rs, 2)

    return False, round(rs, 2)
