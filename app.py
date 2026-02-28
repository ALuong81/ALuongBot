from data.tcbs_client import get_price
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
            message += f"{p['symbol']} | {p['shares']} cp | {round(p['value'],0)} VND\n"

    send_message(message)

    logging.info("Done.")

if __name__ == "__main__":
    main()import logging
from data import get_universe, load_price
from strategy import filter_stocks
from telegram_bot import send_message

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("Fetching data...")

    universe = get_universe()
    selected = []

    # Lấy dữ liệu VNINDEX để tính RS
    index_df = load_price("VNINDEX", is_index=True)

    if index_df is None:
        print("Không lấy được VNINDEX, bỏ qua RS")
        use_rs = False
    else:
        use_rs = True

    for symbol in universe:
        stock_df = load_price(symbol)
        if stock_df is None or len(stock_df) < 200:
            continue

        passed, rs = filter_stocks(symbol, stock_df, index_df)

        if passed:
            current_price = round(stock_df["close"].iloc[-1], 2)

            # % thay đổi hôm nay
            if len(stock_df) > 1:
                change_pct = round(
                    (stock_df["close"].iloc[-1] /
                     stock_df["close"].iloc[-2] - 1) * 100,
                    2
                )
            else:
                change_pct = 0

            selected.append(
                f"{symbol} | {current_price} | {change_pct}% | RS: {rs}"
            )

    # Sắp xếp theo RS giảm dần
    selected.sort(key=lambda x: float(x.split("RS: ")[1]), reverse=True)

    if selected:
        message = "🔥 KẾT QUẢ LỌC CỔ PHIẾU\n\n"
        for stock in selected:
            message += stock + "\n"
    else:
        message = "⚠️ Không có cổ phiếu đạt điều kiện hôm nay."

    send_message(message)

    logging.info("Done.")


if __name__ == "__main__":
    main()



