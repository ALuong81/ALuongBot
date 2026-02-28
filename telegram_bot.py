import os
import requests

def send_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Missing Telegram credentials")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("Telegram message sent.")
    except Exception as e:
        print(f"Telegram error: {e}")

