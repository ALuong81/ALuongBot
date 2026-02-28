def filter_stock(df):
    if df is None or len(df) < 60:
        return False

    ma20 = df["close"].rolling(20).mean().iloc[-1]
    ma50 = df["close"].rolling(50).mean().iloc[-1]
    price = df["close"].iloc[-1]

    return price > ma20 and ma20 > ma50
