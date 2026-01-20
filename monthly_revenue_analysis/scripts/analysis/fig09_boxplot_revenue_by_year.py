import matplotlib.pyplot as plt
import numpy as np
from utils.load_data import load_monthly_revenue


def main():
    df = load_monthly_revenue()

    years = sorted(df["year"].unique())

    data = []
    sample_sizes = []
    for y in years:
        values = df.loc[df["year"] == y, "total_revenue"].to_numpy(dtype=float)
        data.append(values)
        sample_sizes.append(len(values))

    outliers_2011 = None
    if 2011 in years:
        df_2011 = df[df["year"] == 2011]
        values_2011 = df_2011["total_revenue"].to_numpy(dtype=float)

        q1 = np.percentile(values_2011, 25)
        q3 = np.percentile(values_2011, 75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers_2011 = df_2011[
            (df_2011["total_revenue"] < lower_bound) |
            (df_2011["total_revenue"] > upper_bound)
        ].copy()

    fig, ax = plt.subplots(figsize=(9.5, 5.8))

    boxplot = ax.boxplot(
        data,
        tick_labels=[str(y) for y in years],
        showmeans=True,
        patch_artist=True
    )

    ax.set_title(
        "Revenue Distribution by Year Highlights Stability and Variability",
        fontsize=13
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Revenue")
    ax.grid(True, linestyle="--", alpha=0.35)

    whiskers = boxplot["whiskers"]
    medians = boxplot["medians"]
    means = boxplot["means"]

    y_min, y_max = ax.get_ylim()
    y_range = y_max - y_min

    x_min = 0.5
    x_max = len(years) + 0.5
    ax.set_xlim(x_min - 0.55, x_max + 0.55)

    base_x_offset = 0.22 if len(years) <= 4 else 0.16

    for i, n in enumerate(sample_sizes):
        upper_whisker = whiskers[2 * i + 1]
        y_top = max(upper_whisker.get_ydata())
        ax.text(
            i + 1,
            y_top + y_range * 0.03,
            f"n={n}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    bbox_style = dict(
        boxstyle="round,pad=0.15",
        facecolor="white",
        alpha=0.85,
        edgecolor="none"
    )

    for i in range(len(years)):
        median_y = medians[i].get_ydata()[0]
        mean_y = means[i].get_ydata()[0]

        if abs(mean_y - median_y) < y_range * 0.02:
            median_jitter = +y_range * 0.015
            mean_jitter = -y_range * 0.015
        else:
            median_jitter = 0.0
            mean_jitter = 0.0

        x_right = (i + 1) + base_x_offset
        x_left = (i + 1) - base_x_offset

        xlim_left, xlim_right = ax.get_xlim()
        use_right = (x_right + 0.45) <= xlim_right

        if use_right:
            x_text = x_right
            ha = "left"
        else:
            x_text = x_left
            ha = "right"

        ax.text(
            x_text,
            median_y + median_jitter,
            f"median={median_y:,.0f}",
            ha=ha,
            va="center",
            fontsize=8.5,
            color="black",
            bbox=bbox_style
        )
        ax.text(
            x_text,
            mean_y + mean_jitter,
            f"mean={mean_y:,.0f}",
            ha=ha,
            va="center",
            fontsize=8.5,
            color="dimgray",
            bbox=bbox_style
        )

    if outliers_2011 is not None and not outliers_2011.empty:
        year_to_pos = {y: i + 1 for i, y in enumerate(years)}
        pos_2011 = year_to_pos[2011]

        outliers_2011 = outliers_2011.sort_values("total_revenue")

        offsets = [(40, 12), (40, -12), (40, 25), (40, -25)]

        for k, (_, row) in enumerate(outliers_2011.iterrows()):
            label = f"{int(row['year'])}-{int(row['month']):02d}"
            y_out = float(row["total_revenue"])

            dx, dy = offsets[k] if k < len(offsets) else (40, 12)

            ax.annotate(
                label,
                xy=(pos_2011, y_out),
                xytext=(dx, dy),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=9,
                bbox=dict(
                    boxstyle="round,pad=0.25",
                    facecolor="white",
                    alpha=0.9,
                    edgecolor="none"
                ),
                arrowprops=dict(
                    arrowstyle="-|>",
                    lw=0.9,
                    alpha=0.85,
                    shrinkA=6,
                    shrinkB=8
                )
            )

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
