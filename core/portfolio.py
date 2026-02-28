def build_portfolio(results, capital=100000000):
    selected = [r for r in results if r["pass"]]

    if not selected:
        return []

    weight = capital / len(selected)

    portfolio = []

    for stock in selected:
    price_vnd = stock["price"] * 1000
    shares = int(weight / price_vnd)

portfolio.append({
            "symbol": stock["symbol"],
            "price": stock["price"],
            "shares": shares,
            "value": shares * price_vnd
        })

    return portfolio
