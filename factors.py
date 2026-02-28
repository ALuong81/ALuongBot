import numpy as np

def compute_metrics(df):
    df["ret"] = df["close"].pct_change()

    ret_3m = df["close"].pct_change(60).iloc[-1]
    ret_6m = df["close"].pct_change(120).iloc[-1]
    vol = df["ret"].rolling(20).std().iloc[-1]
    liq = df["volume"].rolling(20).mean().iloc[-1]

    return ret_3m, ret_6m, vol, liq

def compute_score(df):
    r3, r6, vol, liq = compute_metrics(df)

    score = (r3 + r6)*0.5 - vol*0.2 + np.log(liq+1)*0.3
    return score, vol