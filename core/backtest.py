import pandas as pd

def backtest(df):
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma50"] = df["close"].rolling(50).mean()

    df["signal"] = (df["close"] > df["ma20"]) & (df["ma20"] > df["ma50"])
    df["return"] = df["close"].pct_change()

    df["strategy_return"] = df["return"] * df["signal"].shift(1)

    total_return = (1 + df["strategy_return"].fillna(0)).cumprod().iloc[-1] - 1

    return round(total_return * 100, 2)
