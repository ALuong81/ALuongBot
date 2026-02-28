import matplotlib.pyplot as plt
import pandas as pd

def plot_equity_curve():
    df = pd.read_csv("nav_history.csv")
    df["date"] = pd.to_datetime(df["date"])

    plt.figure()
    plt.plot(df["date"], df["nav"])
    plt.title("Mini Fund Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("NAV")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("equity.png")
