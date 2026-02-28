import logging
from data import get_universe, get_price
from strategy import filter_stocks
from telegram_bot import send_message

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Fetching data...")

    universe = get_universe()
    selected = []

    for symbol in universe:
        df = get_price(symbol)
        if df is None:
            continue

        if filter_stocks(df):
            selected.append(symbol)

    message = "KẾT QUẢ LỌC CỔ PHIẾU:\n"
    message += "\n".join(selected) if selected else "Không có cổ phiếu đạt điều kiện."

    send_message(message)

    logging.info("Done.")

if __name__ == "__main__":
    main()
