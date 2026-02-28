import pandas as pd
from vnstock import Quote
from config import DATA_START

def get_price(symbol, is_index=False):
    try:
        q = Quote(symbol=symbol, source="VCI")
        df = q.history(start=DATA_START, interval="1D")

        if df is None or df.empty:
            return None

        df.columns = [c.lower() for c in df.columns]
        return df

    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None


def get_universe():
    hose = ["HPG","FPT","MWG","VCB"]
    hnx = ["PVS","SHS"]
    upcom = ["ACV","BSR"]
    return hose + hnx + upcom
