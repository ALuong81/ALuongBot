import requests
import pandas as pd
from datetime import datetime, timedelta

BASE_URL = "https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars"

def get_price(symbol, days=200):
    end = datetime.today()
    start = end - timedelta(days=days)

    params = {
        "ticker": symbol,
        "type": "stock",
        "resolution": "D",
        "from": int(start.timestamp()),
        "to": int(end.timestamp())
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Lỗi TCBS {symbol}")

    data = response.json()

    df = pd.DataFrame({
        "time": data["t"],
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
        "volume": data["v"]
    })

    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.set_index("time", inplace=True)

    return df
