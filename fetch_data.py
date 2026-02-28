import os
import time
from vnstock import Quote

symbols = ["SSI","FPT","HPG","MWG","VCB","BSR","VNINDEX"]

os.makedirs("data", exist_ok=True)

for symbol in symbols:
    try:
        print(f"Fetching {symbol}...")
        q = Quote(symbol=symbol, source="VCI")
        df = q.history(interval="1D")
        df.to_csv(f"data/{symbol}.csv", index=False)
        time.sleep(3)  # tránh rate limit
    except Exception as e:
        print(f"Lỗi {symbol}: {e}")

print("Done fetching.")
