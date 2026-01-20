import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils.load_data import load_monthly_revenue


def main():
    df = load_monthly_revenue()

    # Rolling means
    df["rev_3m"] = df["total_revenue"].rolling(window=3, min_periods=1).mean()
    df["rev_6m"] = df["total_revenue"].rolling(window=6, min_periods=1).mean()

    fig, ax = plt.subplots(figsize=(11, 5))

    ax.plot(
        df["date"],
        df["total_revenue"],
        linewidth=1.3,
        alpha=0.65,
        label="Monthly Revenue"
    )

    ax.plot(
        df["date"],
        df["rev_3m"],
        linewidth=2.2,
        label="3-Month Rolling Mean"
    )
    ax.plot(
        df["date"],
        df["rev_6m"],
        linewidth=2.2,
        linestyle="--",
        label="6-Month Rolling Mean"
    )

    ax.set_title("Rolling Means Reveal Underlying Revenue Trend", fontsize=13)
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Revenue")

    ax.grid(True, linestyle="--", alpha=0.4)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.xticks(rotation=45)

    ax.legend(loc="upper left", frameon=True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
