from vnstock import Vnstock
import pandas as pd
import os

API_KEY = os.getenv("VNSTOCK_API_KEY")

def get_price(symbol, days=200):
    client = Vnstock(api_key=API_KEY)

    stock = client.stock(symbol=symbol, source="VCI")

    df = stock.quote.history(
        start="2023-01-01",
        interval="1D"
    )

    if df.empty:
        raise Exception(f"Không có dữ liệu {symbol}")

    df = df.rename(columns={
        "time": "time",
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close",
        "volume": "volume"
    })

    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)

    return df
