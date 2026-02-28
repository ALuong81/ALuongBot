from core.factors import add_indicators

def filter_stock(symbol, df):
    df = add_indicators(df)

    latest = df.iloc[-1]

    cond1 = latest["close"] > latest["MA20"]
    cond2 = latest["MA20"] > latest["MA50"]
    cond3 = latest["MA50"] > latest["MA200"]

    if cond1 and cond2 and cond3:
        return True, latest["close"]

    return False, latest["close"]
