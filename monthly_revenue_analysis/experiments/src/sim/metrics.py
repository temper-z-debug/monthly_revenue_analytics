from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np


@dataclass(frozen=True)
class RiskMetrics:
    mean: float
    std: float
    var_alpha: float
    cvar_alpha: float
    p_below_T: float
    T: float

    def as_dict(self) -> Dict[str, float]:
        return {
            "mean_R": float(self.mean),
            "std_R": float(self.std),
            "VaR_alpha": float(self.var_alpha),
            "CVaR_alpha": float(self.cvar_alpha),
            "P_below_T": float(self.p_below_T),
            "T": float(self.T),
        }


def compute_risk_metrics(revenue: np.ndarray, alpha: float, T: float) -> RiskMetrics:
    revenue = np.asarray(revenue, dtype=float)
    if revenue.size == 0:
        raise ValueError("revenue array is empty")

    mean = float(np.mean(revenue))
    std = float(np.std(revenue, ddof=1))

    var_alpha = float(np.quantile(revenue, alpha))
    tail = revenue[revenue <= var_alpha]
    cvar = float(np.mean(tail)) if tail.size > 0 else var_alpha

    p_below = float(np.mean(revenue < T))

    return RiskMetrics(mean=mean, std=std, var_alpha=var_alpha, cvar_alpha=cvar, p_below_T=p_below, T=float(T))
