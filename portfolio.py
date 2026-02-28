def allocate(signals):
    capital = 100000000  # 100 triệu
    selected = list(signals.keys())

    if not selected:
        return {}

    weight = capital / len(selected)

    portfolio = {}
    for s in selected:
        portfolio[s] = weight

    return portfolio
