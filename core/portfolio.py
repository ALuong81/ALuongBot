def build_portfolio(passed_stocks, capital=100_000_000):
    portfolio = []

    if not passed_stocks:
        return portfolio

    weight = capital / len(passed_stocks)

    for stock in passed_stocks:
        ticker = stock.get("ticker") or stock.get("symbol")
        price = stock.get("price")

        if not ticker or not price:
            continue

        price_vnd = price * 1000
        shares = int(weight / price_vnd)

        portfolio.append({
            "ticker": ticker,
            "shares": shares,
            "value": shares * price_vnd
        })

    return portfolio
