from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
from scipy.stats import gamma, truncnorm


@dataclass(frozen=True)
class OrdersMarginal:
    mu: float
    sigma: float

    @property
    def dist(self):
        # lower bound 0, upper bound +inf
        a = (0.0 - self.mu) / self.sigma
        b = np.inf
        return truncnorm(a=a, b=b, loc=self.mu, scale=self.sigma)

    def rvs(self, size: int, rng: np.random.Generator) -> np.ndarray:
        return self.dist.rvs(size=size, random_state=rng)

    def ppf(self, u: np.ndarray) -> np.ndarray:
        return self.dist.ppf(u)


@dataclass(frozen=True)
class AOVMarginal:
    shape: float
    scale: float

    @property
    def dist(self):
        return gamma(a=self.shape, scale=self.scale)

    def rvs(self, size: int, rng: np.random.Generator) -> np.ndarray:
        return self.dist.rvs(size=size, random_state=rng)

    def ppf(self, u: np.ndarray) -> np.ndarray:
        return self.dist.ppf(u)


def fit_orders_truncnorm(orders: np.ndarray) -> OrdersMarginal:
    orders = np.asarray(orders, dtype=float)
    mu = float(np.mean(orders))
    sigma = float(np.std(orders, ddof=1))
    if sigma <= 0:
        # fallback to a small sigma to keep distribution valid
        sigma = 1e-6
    return OrdersMarginal(mu=mu, sigma=sigma)


def fit_aov_gamma(aov: np.ndarray) -> AOVMarginal:
    aov = np.asarray(aov, dtype=float)
    m = float(np.mean(aov))
    v = float(np.var(aov, ddof=1))
    if m <= 0 or v <= 0:
        raise ValueError("AOV mean/variance must be positive for Gamma fit")
    shape = (m * m) / v
    scale = v / m
    return AOVMarginal(shape=float(shape), scale=float(scale))


def fit_marginals(orders: np.ndarray, aov: np.ndarray) -> Tuple[OrdersMarginal, AOVMarginal]:
    return fit_orders_truncnorm(orders), fit_aov_gamma(aov)
