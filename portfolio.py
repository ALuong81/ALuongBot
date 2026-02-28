from config import TARGET_VOL, TOP_N_BULL, TOP_N_BEAR

def build_portfolio(scores, regime):

    sorted_items = sorted(scores.items(), key=lambda x: x[1]["score"], reverse=True)

    top_n = TOP_N_BULL if regime=="BULL" else TOP_N_BEAR
    selected = sorted_items[:top_n]

    portfolio = []
    for sym, data in selected:
        vol = data["vol"]
        weight = TARGET_VOL / (vol + 1e-6)
        portfolio.append((sym, data["score"], weight))

    total_weight = sum([x[2] for x in portfolio])
    portfolio = [(s, sc, w/total_weight) for s, sc, w in portfolio]

    return portfolio