from data import get_universe, get_price
from strategy import calculate_signal
from portfolio import allocate
from telegram_bot import send_telegram
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Fetching data...")

    universe = get_universe()
    signals = {}

    for symbol in universe:
        try:
            df = get_price(symbol)
            if calculate_signal(df):
                signals[symbol] = True
        except Exception as e:
            logging.warning(f"{symbol} error: {e}")

    portfolio = allocate(signals)

    message = "<b>📊 STOCK BOT DAILY REPORT</b>\n\n"

    if not portfolio:
        message += "Không có cổ phiếu đạt điều kiện."
    else:
        for s, money in portfolio.items():
            message += f"{s} - Phân bổ: {money:,.0f} VND\n"

    send_telegram(message)
    logging.info("Done.")

if __name__ == "__main__":
    main()from data import get_universe, get_price
from strategy import calculate_signal
from portfolio import allocate
from telegram_bot import send_telegram
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Fetching data...")

    universe = get_universe()
    signals = {}

    for symbol in universe:
        try:
            df = get_price(symbol)
            if calculate_signal(df):
                signals[symbol] = True
        except Exception as e:
            logging.warning(f"{symbol} error: {e}")

    portfolio = allocate(signals)

    message = "<b>📊 STOCK BOT DAILY REPORT</b>\n\n"

    if not portfolio:
        message += "Không có cổ phiếu đạt điều kiện."
    else:
        for s, money in portfolio.items():
            message += f"{s} - Phân bổ: {money:,.0f} VND\n"

    send_telegram(message)
    logging.info("Done.")

if __name__ == "__main__":
    main()

