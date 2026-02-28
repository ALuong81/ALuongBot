import requests
import time
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}

    for _ in range(3):
        try:
            r = requests.post(url, data=payload, timeout=10)
            if r.status_code == 200:
                return
        except:
            time.sleep(2)