from vnstock import Vnstock
import pandas as pd

def get_price(symbol):
    client = Vnstock()

    stock = client.stock(symbol=symbol, source="VCI")

    df = stock.quote.history(
        start="2023-01-01",
        interval="1D"
    )

    if df.empty:
        raise Exception(f"Không có dữ liệu {symbol}")

    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)

    return df
