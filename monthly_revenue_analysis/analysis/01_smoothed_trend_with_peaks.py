import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.interpolate import PchipInterpolator
from utils.load_data import load_monthly_revenue


def main():
    df = load_monthly_revenue()

    x = mdates.date2num(df["date"].to_numpy())
    y = df["total_revenue"].to_numpy(float)

    # Top-2 revenue peaks
    top2 = df["total_revenue"].nlargest(2)
    idx1, idx2 = int(top2.index[0]), int(top2.index[1])

    d1, v1 = df.loc[idx1, "date"], float(df.loc[idx1, "total_revenue"])
    d2, v2 = df.loc[idx2, "date"], float(df.loc[idx2, "total_revenue"])

    # PCHIP smoothing
    interp = PchipInterpolator(x, y)
    x_smooth = np.linspace(x.min(), x.max(), 800)
    y_smooth = interp(x_smooth)

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(mdates.num2date(x_smooth), y_smooth, linewidth=2)
    ax.scatter([d1, d2], [v1, v2], s=70, zorder=5)

    fmt = lambda v: f"{v:,.0f}"

    ax.annotate(
        f"Peak ({d1:%Y-%m})\n{fmt(v1)}",
        xy=(d1, v1),
        xytext=(d1 - pd.Timedelta(days=30), v1*0.9),
        arrowprops=dict(arrowstyle="->"),
        ha="right",
        va="center"
    )

    ax.annotate(
        f"2nd Peak ({d2:%Y-%m})\n{fmt(v2)}",
        xy=(d2, v2),
        xytext=(d2 - pd.Timedelta(days=30), v2*0.93),
        arrowprops=dict(arrowstyle="->"),
        ha="right",
        va="center"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Total Revenue")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.xticks(rotation=45)

    plt.tight_layout()
    fig.subplots_adjust(bottom=0.22)
    plt.show()


if __name__ == "__main__":
    main()
