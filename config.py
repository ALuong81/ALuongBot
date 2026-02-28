import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TARGET_VOL = float(os.getenv("TARGET_VOL", 0.02))
TOP_N_BULL = int(os.getenv("TOP_N_BULL", 5))
TOP_N_BEAR = int(os.getenv("TOP_N_BEAR", 2))

DATA_START = os.getenv("DATA_START", "2018-01-01")
NAV_FILE = "nav.csv"
REGIME_FILE = "regime_history.csv"