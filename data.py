from vnstock import Quote
import pandas as pd


def get_price(symbol, is_index=False):
    try:
        if is_index:
            q = Quote(symbol=symbol, source="VCI", asset_type="index")
        else:
            q = Quote(symbol=symbol, source="VCI")

        df = q.history(interval="1D")

        if df is None or df.empty:
            return None

        df.columns = [c.lower() for c in df.columns]
        return df

    except Exception as e:
        print(f"Lỗi lấy dữ liệu {symbol}: {e}")
        return None


def get_universe():
    hose = ["SSI", "FPT", "HPG", "MWG", "VCB", "BSR"]
    hnx = ["PVS", "SHS"]
    upcom = ["ACV", "OIL"]

    return hose + hnx + upcom
