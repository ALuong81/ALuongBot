import pandas as pd
import os
from datetime import datetime
from config import NAV_FILE, REGIME_FILE

def save_nav(nav):
    today = datetime.today().strftime("%Y-%m-%d")
    df = pd.DataFrame([[today, nav]], columns=["date","nav"])

    if os.path.exists(NAV_FILE):
        df.to_csv(NAV_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(NAV_FILE, index=False)

def save_regime(regime):
    today = datetime.today().strftime("%Y-%m-%d")
    df = pd.DataFrame([[today, regime]], columns=["date","regime"])

    if os.path.exists(REGIME_FILE):
        df.to_csv(REGIME_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(REGIME_FILE, index=False)