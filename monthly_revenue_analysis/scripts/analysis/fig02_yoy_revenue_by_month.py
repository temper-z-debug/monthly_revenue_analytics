import matplotlib.pyplot as plt
from utils.load_data import load_monthly_revenue

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 10,
    "axes.unicode_minus": False
})

def main():
    df = load_monthly_revenue()

    yoy = (
        df.groupby(["year", "month"], as_index=False)["total_revenue"]
        .sum()
        .pivot(index="month", columns="year", values="total_revenue")
        .reindex(range(1, 13))
    )

    fig, ax = plt.subplots(figsize=(11.5, 5))
    months = yoy.index.to_numpy()

    for year in yoy.columns:
        ax.plot(months, yoy[year], marker="o", linewidth=2, label=str(year))

    ax.set_title(
        "Seasonality Pattern Is Consistent Across Years (YoY by Month)",
        fontsize=13
    )

    ax.set_xlabel("Month",fontsize=16)
    ax.set_ylabel("Total Revenue")
    ax.set_xticks(range(1, 13))
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(title="Year", title_fontsize=10, labelspacing=0.4, borderpad=0.6)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
