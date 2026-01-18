import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
from pathlib import Path

from utils.load_data import load_monthly_revenue


def ensure_cols(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "total_revenue" not in df.columns:
        if "revenue" in df.columns:
            df["total_revenue"] = df["revenue"]
        else:
            raise ValueError("Missing total_revenue column")

    if "num_orders" not in df.columns:
        if "orders" in df.columns:
            df["num_orders"] = df["orders"]
        else:
            raise ValueError("Missing num_orders column")

    if "year_month" not in df.columns:
        df["year_month"] = np.arange(len(df)).astype(str)

    return df


def main():
    # ===============================
    # 1. 输出目录（稳定、覆盖写）
    # ===============================
    out_dir = Path("modelling") / "outputs" / "monte_carlo"
    out_dir.mkdir(parents=True, exist_ok=True)

    # ===============================
    # 2. 生成并记录 seed
    # ===============================
    seed = int(time.time())
    rng = np.random.default_rng(seed)

    print(f"\n[Monte Carlo] Random seed = {seed}")

    # ===============================
    # 3. 数据准备
    # ===============================
    df = load_monthly_revenue()
    df = ensure_cols(df)

    df["AOV"] = df["total_revenue"] / df["num_orders"]

    mu_orders = float(df["num_orders"].mean())
    sigma_orders = float(df["num_orders"].std(ddof=1))

    aov_mean = float(df["AOV"].mean())
    aov_std = float(df["AOV"].std(ddof=1))
    aov_var = float(df["AOV"].var(ddof=1))

    if aov_std == 0 or aov_mean == 0:
        raise ValueError("AOV variance or mean is zero")

    shape = (aov_mean / aov_std) ** 2
    scale = aov_var / aov_mean

    # ===============================
    # 4. Monte Carlo simulation
    # ===============================
    n_sim = 50000
    threshold = 1e6

    sim_orders = rng.normal(mu_orders, sigma_orders, n_sim)
    sim_orders = np.clip(sim_orders, 0, None)

    sim_aov = rng.gamma(shape, scale, n_sim)
    sim_revenue = sim_orders * sim_aov

    # ===============================
    # 5. Summary
    # ===============================
    summary = {
        "seed": seed,
        "n_sim": n_sim,
        "orders_mu": mu_orders,
        "orders_sigma": sigma_orders,
        "aov_gamma_shape": shape,
        "aov_gamma_scale": scale,
        "mean_revenue": float(np.mean(sim_revenue)),
        "p05": float(np.percentile(sim_revenue, 5)),
        "p95": float(np.percentile(sim_revenue, 95)),
        "prob_drop_below_1M": float(np.mean(sim_revenue < threshold)),
        "threshold": threshold,
    }

    print("\n=== Monte Carlo Summary ===\n")
    print(pd.Series(summary))

    # ===============================
    # 6. 保存数值结果
    # ===============================
    with open(out_dir / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    sim_df = pd.DataFrame({
        "sim_orders": sim_orders,
        "sim_aov": sim_aov,
        "sim_revenue": sim_revenue,
    })
    sim_df.to_csv(out_dir / "simulations.csv", index=False)

    # ===============================
    # 7. 画 2×2 组图
    # ===============================
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    p05 = summary["p05"]
    p95 = summary["p95"]
    mean_rev = summary["mean_revenue"]

    axes[0, 0].hist(sim_revenue, bins=50, density=True)
    axes[0, 0].axvline(mean_rev, linewidth=2, label="Mean")
    axes[0, 0].axvline(p05, linewidth=2, label="P05")
    axes[0, 0].axvline(p95, linewidth=2, label="P95")
    axes[0, 0].set_title("Revenue Distribution")
    axes[0, 0].legend()

    sorted_rev = np.sort(sim_revenue)
    cdf = np.arange(1, len(sorted_rev) + 1) / len(sorted_rev)
    axes[0, 1].plot(sorted_rev, cdf)
    axes[0, 1].axvline(threshold, linewidth=2, label="Threshold")
    axes[0, 1].set_title("Revenue CDF")
    axes[0, 1].legend()

    axes[1, 0].hist(sim_orders, bins=50, density=True)
    axes[1, 0].set_title("Orders Distribution")

    axes[1, 1].hist(sim_aov, bins=50, density=True)
    axes[1, 1].set_title("AOV Distribution")

    fig.suptitle("Monte Carlo Revenue Simulation", fontsize=14)
    fig.tight_layout()

    # 显示 + 保存
    plt.show()
    fig.savefig(out_dir / "fig_monte_carlo.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    # ===============================
    # 8. README（可选，但很专业）
    # ===============================
    (out_dir / "README.txt").write_text(
        f"Monte Carlo Simulation\n"
        f"Seed: {seed}\n"
        f"Simulations: {n_sim}\n"
        f"Revenue = Orders * AOV\n"
        f"Orders ~ Normal(mu, sigma), clipped at 0\n"
        f"AOV ~ Gamma(shape, scale)\n",
        encoding="utf-8"
    )

    print(f"\nResults saved to: {out_dir.resolve()}")


if __name__ == "__main__":
    main()
