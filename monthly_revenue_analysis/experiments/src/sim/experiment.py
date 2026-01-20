from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils.load_data import load_monthly_revenue

from .copula import estimate_gaussian_copula_rho, gaussian_copula_uniforms
from .distributions import fit_marginals, OrdersMarginal, AOVMarginal
from .metrics import compute_risk_metrics
from .utils import OutputBundle, make_output_bundle, repo_root, sha256_file, try_get_git_commit, write_json

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "experiments" / "outputs"


RESULT_COLUMNS = [
    "exp_id", "scenario", "rho", "n_samples", "seed", "alpha", "T",
    "mean_R", "std_R", "VaR_alpha", "CVaR_alpha", "P_below_T",
]

AGG_COLUMNS = [
    "exp_id", "scenario", "rho", "n_rep", "n_samples", "alpha", "T",
    "VaR_mean", "VaR_std", "VaR_se", "VaR_ci_low", "VaR_ci_high",
    "CVaR_mean", "CVaR_std", "CVaR_se", "CVaR_ci_low", "CVaR_ci_high",
    "Pbelow_mean", "Pbelow_std", "Pbelow_se", "Pbelow_ci_low", "Pbelow_ci_high",
]

def _load_series(csv_path: Path) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    df = pd.read_csv(csv_path)
    df.columns = ["year_month", "total_revenue", "num_orders"]
    orders = df["num_orders"].to_numpy(dtype=float)
    revenue = df["total_revenue"].to_numpy(dtype=float)
    aov = (revenue / orders).astype(float)
    return revenue, orders, aov


def simulate_revenue(
    orders_m: OrdersMarginal,
    aov_m: AOVMarginal,
    rho: float,
    n_samples: int,
    rng: np.random.Generator,
) -> np.ndarray:
    if abs(rho) < 1e-12:
        orders = orders_m.rvs(size=n_samples, rng=rng)
        aov = aov_m.rvs(size=n_samples, rng=rng)
        return orders * aov

    u1, u2 = gaussian_copula_uniforms(n=n_samples, rho=rho, rng=rng)
    orders = orders_m.ppf(u1)
    aov = aov_m.ppf(u2)

    orders = np.clip(orders, 0.0, None)
    aov = np.clip(aov, 0.0, None)
    return orders * aov


def write_results_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=RESULT_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in RESULT_COLUMNS})


def write_results_agg_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=AGG_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in AGG_COLUMNS})


def plot_cdf_with_inset(
    out_png: Path,
    rev_by_label: Dict[str, np.ndarray],
    tail_p_max: float = 0.10,
) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    for label, rev in rev_by_label.items():
        s = np.sort(rev)
        cdf = (np.arange(1, len(s) + 1) / len(s))
        ax.plot(s, cdf, label=label)
    ax.set_title("Revenue CDF sensitivity to dependence (Gaussian copula)")
    ax.set_xlabel("Revenue")
    ax.set_ylabel("CDF")
    ax.legend()

    from mpl_toolkits.axes_grid1.inset_locator import inset_axes

    axins = inset_axes(ax, width="45%", height="45%", loc="lower right")
    for label, rev in rev_by_label.items():
        s = np.sort(rev)
        cdf = (np.arange(1, len(s) + 1) / len(s))
        mask = cdf <= tail_p_max
        axins.plot(s[mask], cdf[mask])
    axins.set_title(f"Tail (p ≤ {tail_p_max:.2f})", fontsize=9)
    axins.set_xlabel("R", fontsize=9)
    axins.set_ylabel("CDF", fontsize=9)

    fig.tight_layout()
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_risk_errorbars(
    out_png: Path,
    rhos: List[float],
    cvar_mean: List[float],
    cvar_ci_low: List[float],
    cvar_ci_high: List[float],
    var_mean: List[float],
    var_ci_low: List[float],
    var_ci_high: List[float],
) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))

    cvar_yerr = np.vstack([
        np.array(cvar_mean) - np.array(cvar_ci_low),
        np.array(cvar_ci_high) - np.array(cvar_mean)
    ])
    ax.errorbar(
        rhos, cvar_mean, yerr=cvar_yerr, fmt="o",
        label="CVaR (95% CI, mean ± 1.96·SE)"
    )

    var_yerr = np.vstack([
        np.array(var_mean) - np.array(var_ci_low),
        np.array(var_ci_high) - np.array(var_mean)
    ])
    ax.errorbar(
        rhos, var_mean, yerr=var_yerr, fmt="o",
        label="VaR (95% CI, mean ± 1.96·SE)"
    )

    ax.set_title("Replicated simulation: tail-risk metrics vs dependence (rho)")
    ax.set_xlabel("rho (Gaussian copula)")

    ax.set_ylabel("Revenue (monetary units)")

    ax.legend()

    fig.tight_layout()
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close(fig)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close(fig)


def _stable_subseed(seed: int, rho: float, tag: int = 0) -> int:
    rho_key = int(round((rho + 1.0) * 1_000_000))
    x = (seed * 1_000_003 + rho_key * 97_129 + tag * 1_389_221) & 0xFFFFFFFF
    return int(x)


def run_copula_rho_sweep(config: Dict[str, Any]) -> OutputBundle:
    repo = repo_root()
    cfg = config
    rel = cfg.get("experiment", {}).get("output_root", None)
    output_root = (PROJECT_ROOT / rel) if rel else DEFAULT_OUTPUT_ROOT

    exp_name = cfg["experiment"]["name"]

    exp_cfg = cfg.get("experiment", {})
    if "seeds" in exp_cfg and exp_cfg["seeds"] is not None:
        seeds = [int(s) for s in exp_cfg["seeds"]]
    else:
        if "seeds" in exp_cfg and exp_cfg["seeds"] is not None:
            seeds = [int(s) for s in exp_cfg["seeds"]]
        else:
            seeds = [int(exp_cfg.get("seed", 42))]

    csv_path = repo / cfg["data"]["monthly_revenue_csv"]
    _, orders, aov = _load_series(csv_path)

    orders_m, aov_m = fit_marginals(orders=orders, aov=aov)

    rho_hat = estimate_gaussian_copula_rho(orders, aov)
    rho_list: List[float] = []
    for item in cfg["model"]["dependence"]["rhos"]:
        rho_list.append(float(rho_hat) if item == "rho_hat" else float(item))

    n_samples = int(cfg["simulation"]["n_samples"])
    alpha = float(cfg["simulation"]["alpha"])

    T_cfg = cfg["simulation"].get("threshold_T", {"type": "auto", "auto_ratio": 0.90})
    T_type = str(T_cfg.get("type", "auto")).lower()
    if T_type == "fixed" and T_cfg.get("value") is not None:
        T = float(T_cfg["value"])
    else:
        auto_ratio = float(T_cfg.get("auto_ratio", 0.90))
        t_seed = int(T_cfg.get("seed", seeds[0]))
        rngT = np.random.default_rng(_stable_subseed(t_seed, rho=0.0, tag=777))
        baseline_rev = simulate_revenue(orders_m, aov_m, rho=0.0, n_samples=n_samples, rng=rngT)
        T = float(np.mean(baseline_rev) * auto_ratio)

    bundle = make_output_bundle(output_root=output_root, exp_name=exp_name)

    rows: List[Dict[str, Any]] = []

    first_seed = seeds[0]
    rev_by_label_first_seed: Dict[str, np.ndarray] = {}

    for seed in seeds:
        for rho in rho_list:
            if abs(rho - rho_hat) <= 1e-9:
                label = f"rho=rho_hat({rho_hat:.2f})"
            else:
                label = f"rho={rho:.2f}"

            rng = np.random.default_rng(_stable_subseed(seed, rho, tag=123))
            rev = simulate_revenue(orders_m, aov_m, rho=rho, n_samples=n_samples, rng=rng)

            if seed == first_seed:
                rev_by_label_first_seed[label] = rev

            m = compute_risk_metrics(rev, alpha=alpha, T=T)
            rows.append({
                "exp_id": exp_name,
                "scenario": label,
                "rho": float(rho),
                "n_samples": n_samples,
                "seed": int(seed),
                "alpha": float(alpha),
                "T": float(T),
                **m.as_dict(),
            })

    write_results_csv(bundle.results_csv, rows)

    if cfg.get("plots", {}).get("cdf", True):
        tail_p_max = float(cfg.get("plots", {}).get("inset_tail", {}).get("p_max", 0.10))
        plot_cdf_with_inset(
            bundle.out_dir / "fig10_cdf_inset.png",
            rev_by_label_first_seed,
            tail_p_max=tail_p_max,
        )

    df = pd.DataFrame(rows)
    agg_rows: List[Dict[str, Any]] = []
    rhos_for_plot: List[float] = []
    cvar_mean: List[float] = []
    cvar_ci_low: List[float] = []
    cvar_ci_high: List[float] = []
    var_mean: List[float] = []
    var_ci_low: List[float] = []
    var_ci_high: List[float] = []

    for (scenario, rho), g in df.groupby(["scenario", "rho"], dropna=False):
        n_rep = int(g["seed"].nunique())
        def _mean_std_se_ci(x: np.ndarray) -> Tuple[float, float, float, float, float]:
            mu = float(np.mean(x))
            sd = float(np.std(x, ddof=1)) if len(x) >= 2 else 0.0
            se = float(sd / math.sqrt(len(x))) if len(x) >= 2 else 0.0
            ci_low = mu - 1.96 * se
            ci_high = mu + 1.96 * se
            return mu, sd, se, ci_low, ci_high

        v_mu, v_sd, v_se, v_lo, v_hi = _mean_std_se_ci(g["VaR_alpha"].to_numpy(dtype=float))
        c_mu, c_sd, c_se, c_lo, c_hi = _mean_std_se_ci(g["CVaR_alpha"].to_numpy(dtype=float))
        p_mu, p_sd, p_se, p_lo, p_hi = _mean_std_se_ci(g["P_below_T"].to_numpy(dtype=float))

        agg_rows.append({
            "exp_id": exp_name,
            "scenario": scenario,
            "rho": float(rho),
            "n_rep": n_rep,
            "n_samples": n_samples,
            "alpha": alpha,
            "T": T,
            "VaR_mean": v_mu, "VaR_std": v_sd, "VaR_se": v_se, "VaR_ci_low": v_lo, "VaR_ci_high": v_hi,
            "CVaR_mean": c_mu, "CVaR_std": c_sd, "CVaR_se": c_se, "CVaR_ci_low": c_lo, "CVaR_ci_high": c_hi,
            "Pbelow_mean": p_mu, "Pbelow_std": p_sd, "Pbelow_se": p_se, "Pbelow_ci_low": p_lo, "Pbelow_ci_high": p_hi,
        })

        rhos_for_plot.append(float(rho))
        cvar_mean.append(c_mu); cvar_ci_low.append(c_lo); cvar_ci_high.append(c_hi)
        var_mean.append(v_mu); var_ci_low.append(v_lo); var_ci_high.append(v_hi)

    order = np.argsort(np.array(rhos_for_plot))
    rhos_for_plot = [rhos_for_plot[i] for i in order]
    cvar_mean = [cvar_mean[i] for i in order]
    cvar_ci_low = [cvar_ci_low[i] for i in order]
    cvar_ci_high = [cvar_ci_high[i] for i in order]
    var_mean = [var_mean[i] for i in order]
    var_ci_low = [var_ci_low[i] for i in order]
    var_ci_high = [var_ci_high[i] for i in order]

    agg_path = bundle.out_dir / "results_agg.csv"
    write_results_agg_csv(agg_path, agg_rows)

    plot_risk_errorbars(
        bundle.out_dir / "fig_risk_errorbars.png",
        rhos_for_plot,
        cvar_mean, cvar_ci_low, cvar_ci_high,
        var_mean, var_ci_low, var_ci_high,
    )

    metadata = {
        "experiment": exp_name,
        "config": cfg,
        "git_commit": try_get_git_commit(repo),
        "data_sha256": sha256_file(csv_path) if csv_path.exists() else None,
        "rho_hat": float(rho_hat),
        "rho_list_resolved": [float(r) for r in rho_list],
        "seeds": seeds,
        "n_samples": n_samples,
        "alpha": alpha,
        "T": T,
        "orders_marginal": {"type": "truncnorm", "mu": orders_m.mu, "sigma": orders_m.sigma},
        "aov_marginal": {"type": "gamma", "shape": aov_m.shape, "scale": aov_m.scale},
        "notes": "CDF plot uses first seed only; results_agg.csv aggregates across seeds with 95% CI = mean ± 1.96*SE."
    }
    write_json(bundle.metadata_json, metadata)
    return bundle


def run_bootstrap_uq(config: Dict[str, Any]) -> OutputBundle:
    repo = repo_root()
    cfg = config
    rel = cfg.get("experiment", {}).get("output_root", None)

    output_root = (PROJECT_ROOT / rel) if rel else DEFAULT_OUTPUT_ROOT

    exp_name = cfg["experiment"]["name"]
    seed = int(cfg["experiment"]["seed"])

    csv_path = repo / cfg["data"]["monthly_revenue_csv"]
    revenue, orders, aov = _load_series(csv_path)

    rho_hat = estimate_gaussian_copula_rho(orders, aov)
    rho_cfg = cfg["model"]["dependence"].get("rho", 0.0)
    rho = rho_hat if rho_cfg == "rho_hat" else float(rho_cfg)

    n_boot = int(cfg["bootstrap"]["n_boot"])
    inner_mc = int(cfg["bootstrap"]["inner_mc"])
    alpha = float(cfg["simulation"]["alpha"])

    rng = np.random.default_rng(seed)

    orders_m0, aov_m0 = fit_marginals(orders, aov)
    rev0 = simulate_revenue(orders_m0, aov_m0, rho=rho, n_samples=inner_mc, rng=np.random.default_rng(seed))
    T0 = float(np.mean(rev0) * 0.90)
    base = compute_risk_metrics(rev0, alpha=alpha, T=T0)

    vars_, cvars_ = [], []
    for b in range(n_boot):
        idx = rng.integers(0, len(revenue), size=len(revenue))
        orders_b = orders[idx]
        aov_b = aov[idx]
        orders_m, aov_m = fit_marginals(orders_b, aov_b)
        rev = simulate_revenue(orders_m, aov_m, rho=rho, n_samples=inner_mc, rng=np.random.default_rng(seed + 1000 + b))
        m = compute_risk_metrics(rev, alpha=alpha, T=T0)
        vars_.append(m.var_alpha)
        cvars_.append(m.cvar_alpha)

    var_lo, var_hi = float(np.quantile(vars_, 0.025)), float(np.quantile(vars_, 0.975))
    cvar_lo, cvar_hi = float(np.quantile(cvars_, 0.025)), float(np.quantile(cvars_, 0.975))

    bundle = make_output_bundle(output_root=output_root, exp_name=exp_name)

    rows = [{
        "exp_id": exp_name,
        "scenario": "point_estimate",
        "rho": float(rho),
        "n_samples": inner_mc,
        "seed": seed,
        "alpha": alpha,
        **base.as_dict(),
    }, {
        "exp_id": exp_name,
        "scenario": "bootstrap_interval",
        "rho": float(rho),
        "n_samples": inner_mc,
        "seed": seed,
        "alpha": alpha,
        "T": float(T0),
        "mean_R": float(base.mean),
        "std_R": float(base.std),
        "VaR_alpha": float(base.var_alpha),
        "CVaR_alpha": float(base.cvar_alpha),
        "P_below_T": float(base.p_below_T),
    }]

    write_results_csv(bundle.results_csv, rows)

    if cfg.get("plots", {}).get("interval_plot", True):
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.errorbar(["VaR"], [base.var_alpha], yerr=[[base.var_alpha - var_lo], [var_hi - base.var_alpha]], fmt="o")
        ax.errorbar(["CVaR"], [base.cvar_alpha], yerr=[[base.cvar_alpha - cvar_lo], [cvar_hi - base.cvar_alpha]], fmt="o")
        ax.set_title("Bootstrap UQ: parameter uncertainty intervals")
        ax.set_ylabel("Value")
        fig.tight_layout()
        fig.savefig(bundle.out_dir / "fig_uq_interval.png", dpi=200, bbox_inches="tight")
        plt.close(fig)

    metadata = {
        "experiment": exp_name,
        "config": cfg,
        "git_commit": try_get_git_commit(repo),
        "data_sha256": sha256_file(csv_path) if csv_path.exists() else None,
        "rho_used": float(rho),
        "rho_hat": float(rho_hat),
        "n_boot": n_boot,
        "inner_mc": inner_mc,
        "intervals": {
            "VaR_95": [var_lo, var_hi],
            "CVaR_95": [cvar_lo, cvar_hi],
        },
    }
    write_json(bundle.metadata_json, metadata)
    return bundle


def run_decision_threshold(config: Dict[str, Any]) -> OutputBundle:
    repo = repo_root()
    cfg = config
    rel = cfg.get("experiment", {}).get("output_root", None)

    output_root = (PROJECT_ROOT / rel) if rel else DEFAULT_OUTPUT_ROOT

    exp_name = cfg["experiment"]["name"]
    seed = int(cfg["experiment"]["seed"])

    csv_path = repo / cfg["data"]["monthly_revenue_csv"]
    _, orders, aov = _load_series(csv_path)
    orders_m, aov_m = fit_marginals(orders, aov)

    rho_cfg = cfg["model"]["dependence"].get("rho", 0.0)
    rho = float(rho_cfg)

    n_samples = int(cfg["simulation"]["n_samples"])
    risk_alpha = float(cfg["decision"]["risk_alpha"])

    rng = np.random.default_rng(seed)
    rev = simulate_revenue(orders_m, aov_m, rho=rho, n_samples=n_samples, rng=rng)

    mean_R = float(np.mean(rev))
    T_min = float(cfg["decision"]["T_search"].get("T_min_ratio", 0.0)) * mean_R
    T_max = float(cfg["decision"]["T_search"].get("T_max_ratio", 1.5)) * mean_R
    tol = float(cfg["decision"]["T_search"].get("tol", 1e-3)) * mean_R
    max_iter = int(cfg["decision"]["T_search"].get("max_iter", 40))

    def p_below(t: float) -> float:
        return float(np.mean(rev < t))

    lo, hi = T_min, T_max
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        if (hi - lo) <= tol:
            break
        if p_below(mid) <= risk_alpha:
            hi = mid
        else:
            lo = mid

    T_star = float(hi)
    m = compute_risk_metrics(rev, alpha=0.05, T=T_star)

    bundle = make_output_bundle(output_root=output_root, exp_name=exp_name)
    write_results_csv(bundle.results_csv, [{
        "exp_id": exp_name,
        "scenario": "bisection_threshold",
        "rho": float(rho),
        "n_samples": n_samples,
        "seed": seed,
        "alpha": 0.05,
        **m.as_dict(),
    }])

    if cfg.get("plots", {}).get("threshold_curve", True):
        s = np.sort(rev)
        cdf = (np.arange(1, len(s) + 1) / len(s))
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(s, cdf, label="Empirical CDF")
        ax.axhline(risk_alpha, linewidth=2, label=f"risk_alpha={risk_alpha:.2f}")
        ax.axvline(T_star, linewidth=2, label=f"T*={T_star:.0f}")
        ax.set_title("Risk constraint: find minimal T such that P(R<T) ≤ risk_alpha")
        ax.set_xlabel("T")
        ax.set_ylabel("P(R<T)")
        ax.legend()
        fig.tight_layout()
        fig.savefig(bundle.out_dir / "fig_threshold_curve.png", dpi=200, bbox_inches="tight")
        plt.close(fig)

    metadata = {
        "experiment": exp_name,
        "config": cfg,
        "git_commit": try_get_git_commit(repo),
        "data_sha256": sha256_file(csv_path) if csv_path.exists() else None,
        "rho_used": float(rho),
        "risk_alpha": risk_alpha,
        "T_star": T_star,
    }
    write_json(bundle.metadata_json, metadata)
    return bundle
