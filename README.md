# Monthly Revenue Analytics

This repository presents a reproducible, script-driven workflow for analyzing monthly revenue dynamics and evaluating both predictive and simulation-based approaches. I built it as a portfolio-quality project that prioritizes clear assumptions, traceable execution, and reviewable artifacts—so a reviewer can understand what I did, why I did it, and how to reproduce it.

The main pipeline generates figures and metrics from code under `monthly_revenue_analysis/`. Optional research-style extensions (config-driven experiments) live under `monthly_revenue_analysis/experiments/`.

---

## Project Questions

- How does revenue evolve over time (trend and seasonality)?
- Are revenue changes driven more by order volume or by AOV (basket size)?
- How well can we predict revenue with time-consistent evaluation (no shuffle)?
- How uncertain are outcomes, and what do tail behaviors look like under simulation?

---

## Methodology Overview

- **Trend and seasonality diagnostics**: smoothing, peak identification, month-aligned YoY views, rolling-window summaries, and distributional checks.
- **Driver decomposition**: interpretability-first factorization with `Revenue = Orders × AOV`.
- **Predictive modeling (time-consistent evaluation)**: lag features + calendar encodings; chronological holdout split to avoid temporal leakage.
- **Stochastic simulation (uncertainty and tail behavior)**: parametric uncertainty for Orders and AOV; Monte Carlo draws for uncertainty and tail summaries.
- **Reproducibility**: centralized data loading, deterministic seeds, and standardized artifact writing.

---

## Repository Structure


```
monthly_revenue_analysis/
│
├── data/                  # Processed data (raw data excluded)
├── utils/                 # Data loaders, plot styling, helper utilities
├── scripts/               # Main pipeline scripts
│     ├── analysis/        # Fig.01–Fig.09 (trend/seasonality/driver diagnostics)
│     └── modeling/        # Fig.10–Fig.11 (models + simulation)
├── sql/                   # SQL ETL pipeline (raw transactions → cleaned monthly panel) + validation checks
├── experiments/           # Config-driven experiments (copula stress test, bootstrap UQ, decision threshold)
├── figures/               # Generated figures (Fig.01–Fig.11)
└── run_all.py # One-click runner for the main pipeline
```


A more detailed mapping between scripts and output figures is provided in:
`monthly_revenue_analysis/README.md`

---

## Data Source

This project is based on the Online Retail II transactional dataset (UCI Machine Learning Repository):

Chen, D. (2015). Online Retail II Data Set.  
https://archive.ics.uci.edu/dataset/352/online+retail

The raw transaction-level CSV is not included in this repository (licensing / size considerations). This repo includes the cleaned and aggregated monthly dataset used by all Python scripts:

- `monthly_revenue_analysis/data/processed/monthly_revenue.csv`

---

## Data Cleaning and ETL (SQL)

Transaction-level records are transformed into a monthly panel using SQL scripts in `monthly_revenue_analysis/sql/`. The goal is to remove non-economic entries and produce a clean, interpretable time series.

Step 1 — Raw ingestion
- Import the raw CSV into MySQL staging tables (see `sql/00_setup.sql` and `sql/01_load_raw_online_retail.sql`).
- Ingest without transformation to preserve original fields.

Step 2 — Transaction filtering
Remove invalid or non-economic records:
- Cancelled invoices removed: exclude `InvoiceNo` starting with 'C'
- Returns/corrections removed: exclude `Quantity <= 0`
- Invalid pricing removed: exclude `UnitPrice <= 0`
- Missing customer identifiers removed: exclude `CustomerID IS NULL`

Step 3 — Revenue computation
- Compute line-item revenue: `Revenue = Quantity × UnitPrice`

Step 4 — Monthly aggregation
- Convert `InvoiceDate` to `YYYYMM`
- Aggregate:
  - `total_revenue = Σ Revenue`
  - `num_orders = COUNT(DISTINCT InvoiceNo)`

Step 5 — Validation checks
- Sanity checks are implemented in `sql/04_validation_checks.sql` (coverage checks, negative/zero revenue detection, summary consistency).

For exact MySQL setup and execution order, see:
- `monthly_revenue_analysis/sql/README.md`

---

## Reproducible Runs

Install dependencies (from the repository root):
- pip install -r requirements.txt

One-click main pipeline (recommended):
- python monthly_revenue_analysis/run_all.py --save

Run a single script (example):
- python monthly_revenue_analysis/scripts/analysis/fig01_smoothed_trend.py

Run modeling & simulation modules:
- python monthly_revenue_analysis/scripts/modeling/10_model_comparison_LR_RF.py
- python monthly_revenue_analysis/scripts/modeling/11_monte_carlo_simulation.py

Note on dataset size:
The monthly panel covers a limited time span (roughly 2010–2011, ~24 monthly observations). The modeling focus is therefore on interpretability, time-consistent evaluation, and uncertainty quantification rather than high-capacity forecasting.

---

## Outputs

When running with `--save`, artifacts are written to:
- monthly_revenue_analysis/outputs/latest/figures/
- monthly_revenue_analysis/outputs/latest/metrics/

If `outputs/` does not exist, it is created automatically. These runtime artifacts are generated for reproduction and review and are typically excluded from version control.

---

## Advanced Experiments (Optional)

The `monthly_revenue_analysis/experiments/` folder contains config-driven, research-style experiments that extend the main pipeline:
- Copula dependence sweep: counterfactual dependence stress test (holding marginals fixed)
- Bootstrap uncertainty quantification: parameter uncertainty intervals for key metrics
- Decision threshold loop: simple risk-constraint style search based on empirical simulation outputs

Run an experiment (example):
- python monthly_revenue_analysis/experiments/scripts/run_experiment.py --config monthly_revenue_analysis/experiments/configs/exp_copula_rho_sweep.yaml

Experiment outputs are written to:
- monthly_revenue_analysis/experiments/outputs/<timestamp>_<experiment_name>/

The output directory is created automatically if missing.

---

## Report

A consolidated PDF report (figures + narrative) is available at:
- monthly_revenue_analysis.pdf

---

## Author

Zhong Yuyang  
Email: zhongyuyangm4@gmail.com

---

## License

MIT License


MIT License
