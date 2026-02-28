from data.vnstock_client import get_price
from core.strategy import filter_stock
from core.portfolio import build_portfolio
from infra.telegram_bot import send_message

import logging

logging.basicConfig(level=logging.INFO)

SYMBOLS = ["SSI","FPT","HPG","MWG","VCB","BSR"]

def main():
    logging.info("Fetching data...")

    results = []

    for symbol in SYMBOLS:
        try:
            df = get_price(symbol)
            passed, price = filter_stock(symbol, df)

            results.append({
                "symbol": symbol,
                "pass": passed,
                "price": price
            })

        except Exception as e:
            print(f"Lỗi {symbol}: {e}")

    portfolio = build_portfolio(results)

    message = "📊 KẾT QUẢ LỌC CỔ PHIẾU\n\n"

    for r in results:
        status = "✅" if r["pass"] else "❌"
        message += f"{status} {r['symbol']} - Giá: {round(r['price'],2)}\n"

    if portfolio:
        message += "\n💰 DANH MỤC MINI FUND\n"
        for p in portfolio:
            ticker = p.get("ticker") or p.get("symbol")
            message += f"{ticker} | {p['shares']} cp | {round(p['value'],0)} VND\n"
    print(message)
    send_message(message)

    logging.info("Done.")

if __name__ == "__main__":
    main()



