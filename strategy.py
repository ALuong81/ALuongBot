import pandas as pd
import numpy as np

def calculate_signal(df):
    df["MA20"] = df["close"].rolling(20).mean()
    df["MA50"] = df["close"].rolling(50).mean()

    latest = df.iloc[-1]

    if latest["close"] > latest["MA20"] > latest["MA50"]:
        return True
    return False
