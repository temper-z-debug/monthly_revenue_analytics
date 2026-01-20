import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from utils.load_data import load_monthly_revenue
from utils.plot_utils import add_takeaway

def main():
    df = load_monthly_revenue()

    X = df["num_orders"].values.reshape(-1, 1)
    y = df["total_revenue"].values

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    fig, ax = plt.subplots(figsize=(11, 6))

    ax.scatter(
        df["num_orders"],
        df["total_revenue"],
        s=55,
        alpha=0.8,
        label="Monthly Observations"
    )

    order_sorted = np.argsort(X.flatten())
    ax.plot(
        X.flatten()[order_sorted],
        y_pred[order_sorted],
        linestyle="--",
        linewidth=2.2,
        label="Linear Fit"
    )

    top2 = df["total_revenue"].nlargest(2)
    offsets = [(-30, 0), (-30, -18)]

    for k, idx in enumerate(top2.index):
        orders = int(df.loc[idx, "num_orders"])
        rev = float(df.loc[idx, "total_revenue"])
        label = df.loc[idx, "date"].strftime("%Y-%m")

        dx, dy = offsets[k] if k < len(offsets) else (-45, 18)

        ax.annotate(
            label,
            xy=(orders, rev),
            xytext=(dx, dy),
            textcoords="offset points",
            ha="right",
            va="center",
            fontsize=9,
            arrowprops=dict(arrowstyle="-", linewidth=0.8, alpha=0.8)
        )

    ax.set_title("Revenue vs Orders Suggests Strong Volume–Revenue Link", fontsize=13)
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("Total Revenue")
    ax.grid(True, linestyle="--", alpha=0.4)

    ax.text(
        0.27, 0.95,
        f"$R^2 = {r2:.2f}$",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
        bbox=dict(
            boxstyle="round,pad=0.25",
            facecolor="white",
            alpha=0.85,
            edgecolor="none"
        )
    )

    ax.legend(loc="upper left", frameon=True)

    add_takeaway(
        ax,
        "Revenue exhibits a strong linear relationship with order volume, supported by a high R², confirming volume-led growth dynamics."
    )

    fig.subplots_adjust(bottom=0.15)
    plt.show()


if __name__ == "__main__":
    main()
