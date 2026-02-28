import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)


def send_photo(path: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    with open(path, "rb") as f:
        requests.post(
            url,
            data={"chat_id": TELEGRAM_CHAT_ID},
            files={"photo": f}
        )
