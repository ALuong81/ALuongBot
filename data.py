import pandas as pd
import os

def load_price(symbol):
    path = f"data/{symbol}.csv"
    if not os.path.exists(path):
        return None

    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]
    return df
