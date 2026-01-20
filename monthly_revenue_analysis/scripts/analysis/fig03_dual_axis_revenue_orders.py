import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils.load_data import load_monthly_revenue

def main():
    df = load_monthly_revenue()

    fig, ax1 = plt.subplots(figsize=(11, 5))
    ax2 = ax1.twinx()

    line1, = ax1.plot(
        df["date"],
        df["total_revenue"],
        color="#1f77b4",      # 深蓝
        linewidth=2.5,
        label="Total Revenue"
    )

    line2, = ax2.plot(
        df["date"],
        df["num_orders"],
        color="#ff7f0e",      # 橙色
        linewidth=2.0,
        linestyle="--",
        label="Number of Orders"
    )

    ax1.set_title(
        "Revenue Growth Is Primarily Driven by Order Volume",
        fontsize=13
    )

    ax1.set_xlabel("Month",fontsize=16)
    ax1.set_ylabel("Total Revenue", color="#1f77b4")
    ax2.set_ylabel("Number of Orders", color="#ff7f0e")

    ax1.tick_params(axis="y", labelcolor="#1f77b4")
    ax2.tick_params(axis="y", labelcolor="#ff7f0e")

    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax1.tick_params(axis="x", rotation=45)

    ax1.grid(True, linestyle="--", alpha=0.4)

    lines = [line1, line2]
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc="best", frameon=True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
