import pandas as pd
from vnstock import stock_historical_data
from config import DATA_START

def get_price(symbol, is_index=False):
    try:
        df = stock_historical_data(
            symbol=symbol,
            start_date=DATA_START,
            end_date=None,
            resolution="1D",
            type="index" if is_index else "stock",
            beautify=True,
        )
        return df
    except:
        return None

def get_universe():
    hose = ["HPG","FPT","MWG","VCB"]
    hnx = ["PVS","SHS"]
    upcom = ["ACV","BSR"]
    return hose + hnx + upcom