def build_portfolio(passed_stocks, capital=100_000_000):
    portfolio = []
    
    if not passed_stocks:
        return portfolio

    weight = capital / len(passed_stocks)

    for stock in passed_stocks:
        price_vnd = stock["price"] * 1000   # đổi từ nghìn sang VND
        shares = int(weight / price_vnd)

        portfolio.append({
            "ticker": stock["ticker"],
            "shares": shares,
            "value": shares * price_vnd
        })

    return portfolio
