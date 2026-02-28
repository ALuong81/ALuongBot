import pandas as pd
from datetime import datetime, timedelta
from core.strategy import filter_stock
from core.portfolio import build_portfolio
from core.regime import market_regime
from data.vnstock_client import get_price

def run_backtest(symbols, start_date, end_date, capital=100_000_000):
    dates = pd.date_range(start_date, end_date, freq="M")
    nav = capital
    nav_history = []

    for date in dates:
        results = []

        for symbol in symbols:
            df = get_price(symbol, start=start_date, end=date.strftime("%Y-%m-%d"))
            if df is None or len(df) < 50:
                continue

            passed = filter_stock(df)
            price = df["close"].iloc[-1]

            results.append({
                "symbol": symbol,
                "pass": passed,
                "price": float(price)
            })

        regime = market_regime()

        portfolio = build_portfolio(results, capital=nav, regime=regime)

        nav = sum(p["value"] for p in portfolio)

        nav_history.append({
            "date": date,
            "nav": nav
        })

    return pd.DataFrame(nav_history)
