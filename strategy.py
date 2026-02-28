import pandas as pd

def filter_stocks(df):
    if df is None or len(df) < 50:
        return False

    df = df.copy()

    # Tính MA20
    df["ma20"] = df["close"].rolling(20).mean()

    # Điều kiện:
    # 1. Giá hiện tại > MA20
    # 2. Volume hôm nay > volume trung bình 20 phiên

    latest = df.iloc[-1]
    avg_volume = df["volume"].rolling(20).mean().iloc[-1]

    cond1 = latest["close"] > latest["ma20"]
    cond2 = latest["volume"] > avg_volume

    return cond1 and cond2
