import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils.load_data import load_monthly_revenue

def main():
    df = load_monthly_revenue()

    # MoM growth
    df["mom"] = df["total_revenue"].pct_change(1) * 100

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(df["date"], df["mom"], linewidth=2, color="#9467bd")

    ax.set_title("MoM Revenue Growth Shows Short-Term Volatility", fontsize=13)

    ax.set_xlabel("Month")
    ax.set_ylabel("MoM Growth Rate (%)")
    ax.axhline(0, color="gray", linestyle="--", linewidth=1)

    ax.grid(True, linestyle="--", alpha=0.4)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
