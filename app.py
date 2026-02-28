from data import get_universe, get_price
from factors import compute_score
from regime import detect_regime
from portfolio import build_portfolio
from telegram_bot import send_message
from storage import save_nav, save_regime
from logger import get_logger

logger = get_logger()

def main():

    universe = get_universe()
    scores = {}

    logger.info("Fetching data...")

    for symbol in universe:
        df = get_price(symbol)
        if df is None or len(df)<200:
            continue

        score, vol = compute_score(df)
        scores[symbol] = {"score": score, "vol": vol}

    index_df = get_price("VNINDEX", is_index=True)
    regime = detect_regime(index_df)

    portfolio = build_portfolio(scores, regime)

    nav = 1.0  # demo NAV cố định, có thể tính real sau
    save_nav(nav)
    save_regime(regime)

    message = f"VN MINI FUND\nRegime: {regime}\n\n"
    for sym, sc, w in portfolio:
        message += f"{sym} | Score {round(sc,3)} | Weight {round(w,2)}\n"

    send_message(message)
    logger.info("Done.")

if __name__ == "__main__":
    main()