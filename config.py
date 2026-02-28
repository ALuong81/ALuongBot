import os

# ==============================
# 1. DANH SÁCH CỔ PHIẾU THEO DÕI
# ==============================

SYMBOLS = [
    "SSI",
    "FPT",
    "HPG",
    "MWG",
    "VCB",
    "BSR"
]

# Có thể tách theo sàn nếu muốn scale
HOSE = ["SSI", "FPT", "HPG", "MWG", "VCB"]
HNX = []
UPCOM = ["BSR"]


# ==============================
# 2. CẤU HÌNH CHIẾN LƯỢC
# ==============================

MA_SHORT = 20
MA_MID = 50
MA_LONG = 200

USE_MARKET_FILTER = True   # Lọc theo VNINDEX > MA200
MAX_STOCKS = 5             # Tối đa bao nhiêu mã trong danh mục


# ==============================
# 3. QUỸ MINI
# ==============================

INITIAL_CAPITAL = 100_000_000   # 100 triệu VND
MAX_POSITION_PCT = 0.25         # tối đa 25% mỗi mã


# ==============================
# 4. TELEGRAM
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# ==============================
# 5. TCBS DATA
# ==============================

TCBS_BASE_URL = "https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars"


# ==============================
# 6. LOGGING
# ==============================

LOG_LEVEL = "INFO"

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

