import logging
from data.vnstock_client import get_price
from core.strategy import filter_stock
from core.regime import market_regime
from core.portfolio import build_portfolio
from core.risk import capital_allocation
from infra.telegram_bot import send_message

logging.basicConfig(level=logging.INFO)

WATCHLIST = ["SSI","FPT","HPG","MWG","VCB","BSR"]
TOTAL_CAPITAL = 100_000_000

def main():
    logging.info("Fetching data...")

    results = []

    for symbol in WATCHLIST:
        df = get_price(symbol)
        if df is None:
            continue

        passed = filter_stock(df)
        price = df["close"].iloc[-1]

        results.append({
            "ticker": symbol,
            "price": float(price),
            "passed": passed
        })

    logging.info("Done.")

    message = "📊 KẾT QUẢ LỌC CỔ PHIẾU\n"

    for r in results:
        icon = "✅" if r["passed"] else "❌"
        message += f"{icon} {r['ticker']} - Giá: {r['price']}\n"

    passed_stocks = [r for r in results if r["passed"]]

    if passed_stocks:
        allocated_capital = capital_allocation(TOTAL_CAPITAL, "BULL")
        portfolio = build_portfolio(passed_stocks, allocated_capital)
    
        from storage import save_nav
        total_nav = sum(p["value"] for p in portfolio)
        save_nav(total_nav)

        message += "\n💰 DANH MỤC MINI FUND\n"
        for p in portfolio:
            message += f"{p['ticker']} | {p['shares']} cp | {round(p['value'],0)} VND\n"

    send_message(message)
    print(message)
 
    from core.report import plot_equity_curve
    from infra.telegram_bot import send_photo

    plot_equity_curve()
    send_photo("equity.png")

if __name__ == "__main__":
    main()




