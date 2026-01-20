from __future__ import annotations

from typing import Tuple

import numpy as np
from scipy.stats import norm


def estimate_gaussian_copula_rho(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if n != len(y) or n < 3:
        raise ValueError("x and y must have same length and at least 3 samples")

    rx = np.argsort(np.argsort(x)) + 1
    ry = np.argsort(np.argsort(y)) + 1
    ux = (rx - 0.5) / n
    uy = (ry - 0.5) / n

    zx = norm.ppf(ux)
    zy = norm.ppf(uy)

    rho = float(np.corrcoef(zx, zy)[0, 1])
    # clip for numerical stability
    return float(np.clip(rho, -0.99, 0.99))


def gaussian_copula_normals(n: int, rho: float, rng: np.random.Generator) -> Tuple[np.ndarray, np.ndarray]:
    rho = float(np.clip(rho, -0.99, 0.99))
    cov = np.array([[1.0, rho], [rho, 1.0]], dtype=float)
    L = np.linalg.cholesky(cov)
    z = rng.standard_normal(size=(2, n))
    corr = L @ z
    return corr[0], corr[1]


def gaussian_copula_uniforms(n: int, rho: float, rng: np.random.Generator) -> Tuple[np.ndarray, np.ndarray]:
    z1, z2 = gaussian_copula_normals(n=n, rho=rho, rng=rng)
    u1 = norm.cdf(z1)
    u2 = norm.cdf(z2)
    # protect against exact 0/1
    eps = np.finfo(float).eps
    u1 = np.clip(u1, eps, 1 - eps)
    u2 = np.clip(u2, eps, 1 - eps)
    return u1, u2
