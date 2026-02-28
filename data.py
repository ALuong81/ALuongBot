from vnstock import Vnstock
import pandas as pd

def get_universe():
    # 3 sàn
    return [
        "VCB","BID","CTG","HPG","FPT","MWG","VNM",
        "SSI","VND","GAS","PLX","PVD","HSG",
        "REE","PNJ","DXG","NLG","KDH"
    ]

def get_price(symbol):
    stock = Vnstock().stock(symbol=symbol, source="VCI")
    df = stock.quote.history(start="2023-01-01", interval="1D")
    return df
