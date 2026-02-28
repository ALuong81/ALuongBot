def detect_regime(index_df):
    ma200 = index_df["close"].rolling(200).mean()
    price = index_df["close"].iloc[-1]

    if price > ma200.iloc[-1]:
        return "BULL"
    return "BEAR"