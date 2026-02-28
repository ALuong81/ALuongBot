def build_portfolio(results, capital=100000000):
    selected = [r for r in results if r["pass"]]

    if not selected:
        return []

    weight = capital / len(selected)

    portfolio = []

    for stock in selected:
        shares = int(weight / stock["price"])

        portfolio.append({
            "symbol": stock["symbol"],
            "price": stock["price"],
            "shares": shares,
            "value": shares * stock["price"]
        })

    return portfolio
