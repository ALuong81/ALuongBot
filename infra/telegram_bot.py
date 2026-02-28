import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_photo(path):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    with open(path, "rb") as f:
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID}, files={"photo": f})
