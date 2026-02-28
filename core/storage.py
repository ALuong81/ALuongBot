import pandas as pd
import os

NAV_FILE = "nav_history.csv"

def save_nav(value):
    today = pd.Timestamp.today().date()

    if os.path.exists(NAV_FILE):
        df = pd.read_csv(NAV_FILE)
    else:
        df = pd.DataFrame(columns=["date", "nav"])

    df = pd.concat([df, pd.DataFrame([{
        "date": today,
        "nav": value
    }])])

    df.to_csv(NAV_FILE, index=False)
