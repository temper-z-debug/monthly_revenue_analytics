import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils.load_data import load_monthly_revenue


def main():
    df = load_monthly_revenue()

    df["aov"] = df["total_revenue"] / df["num_orders"]

    fig, ax = plt.subplots(figsize=(11, 5))

    ax.plot(df["date"], df["aov"], linewidth=2, color="#2ca02c")
    ax.set_title("Average Order Value Remains Stable Over Time", fontsize=13)
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Order Value (AOV)")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.xticks(rotation=45)

    plt.tight_layout()
    fig.subplots_adjust(bottom=0.22)
    plt.show()


if __name__ == "__main__":
    main()
