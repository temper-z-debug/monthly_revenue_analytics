import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils.load_data import load_monthly_revenue
from utils.plot_theme import apply_portfolio_theme


def main():
    apply_portfolio_theme("Segoe UI")  # 全作品集统一风格

    df = load_monthly_revenue()
    df = df.sort_values("date").reset_index(drop=True)
    df["yoy_growth"] = df["total_revenue"].pct_change(periods=12)
    df_yoy = df.dropna(subset=["yoy_growth"]).copy()

    fig, ax = plt.subplots(figsize=(10.5, 5.3))

    ax.plot(df_yoy["date"], df_yoy["yoy_growth"] * 100, marker="o", linewidth=2)
    ax.axhline(0, linestyle="--", linewidth=1, alpha=0.4)

    ax.set_title("YoY Growth Rate Reflects Demand Cycles Over Time")  # 标题更自然
    ax.set_xlabel("Month")
    ax.set_ylabel("YoY Growth Rate (%)")

    # 可选：更清晰的日期轴
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.tick_params(axis="x", rotation=45)

    plt.show()

if __name__ == "__main__":
    main()
