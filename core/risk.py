def capital_allocation(total_capital, regime):
    if regime == "BULL":
        return total_capital
    elif regime == "BEAR":
        return total_capital * 0.4
    else:
        return total_capital * 0.5
