# Monthly Revenue Analytics

This repository contains a reproducible data analysis and modeling workflow for monthly revenue data.
The objective is to characterize revenue dynamics, quantify underlying drivers, and evaluate predictive and stochastic models in a controlled, well-structured environment.

The codebase is modular and script-driven (rather than notebook-first) to keep the workflow traceable and easy to re-run.
All figures, metrics, and intermediate artifacts are generated directly from the scripts under `monthly_revenue_analysis/`.

---

## Key Methodology

- **Trend and seasonality diagnostics**
  Smoothing, peak identification, month-aligned YoY comparisons, rolling-window summaries, and distributional views to isolate cyclic structure and regime shifts.

- **Deterministic driver decomposition**
  Revenue is analyzed as `Revenue = Orders × AOV` to separate volume-driven effects from basket/price-driven effects.

- **Predictive modeling (time-consistent evaluation)**
  Linear Regression and Random Forest models using lag features and calendar encodings.
  Evaluation uses a chronological holdout split (no random shuffle) to preserve time consistency.

- **Stochastic simulation (uncertainty and tail behavior)**
  Orders and AOV are modeled with parametric distributions and sampled via Monte Carlo to estimate uncertainty, downside probability, and tail risk summaries.

- **Reproducibility**
  Deterministic seeds, centralized data loading, and standardized artifact writing ensure consistent runs across environments.

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

The raw transaction-level CSV is not included in this repository (licensing / size considerations).
This repo includes a cleaned and aggregated monthly panel used by the Python scripts:

- `monthly_revenue_analysis/data/processed/monthly_revenue.csv`

---

## Data Cleaning and ETL Pipeline (SQL)

Transaction-level records are transformed into a monthly revenue panel using SQL scripts in `monthly_revenue_analysis/sql/`.
The goal is to remove non-economic entries and produce a clean time series suitable for trend diagnostics and forecasting-style evaluation.

Step 1 — Raw ingestion  
- Import the raw CSV into MySQL staging tables (see `sql/00_setup.sql` and `sql/01_load_raw_online_retail.sql`).
- Ingest fields without transformation to preserve original information.

Step 2 — Transaction filtering  
Remove invalid or non-economic records:
- **Cancelled invoices removed**: exclude rows where `InvoiceNo` starts with `'C'`.
- **Returns/corrections removed**: exclude rows where `Quantity <= 0`.
- **Invalid pricing removed**: exclude rows where `UnitPrice <= 0`.
- **Missing customer identifiers removed**: exclude rows where `CustomerID IS NULL`.

Step 3 — Revenue computation  
- Compute line-item revenue: `Revenue = Quantity × UnitPrice`.

Step 4 — Monthly aggregation  
- Convert `InvoiceDate` to `YYYYMM`.
- Aggregate to monthly:
  - `total_revenue = Σ Revenue`
  - `num_orders = COUNT(DISTINCT InvoiceNo)`

Step 5 — Validation checks  
- Sanity checks are implemented in `sql/04_validation_checks.sql` (coverage checks, negative/zero revenue detection, summary consistency).

The final analytical dataset is stored at:
- `monthly_revenue_analysis/data/processed/monthly_revenue.csv`

Schema:
- `year_month` (YYYYMM)
- `total_revenue`
- `num_orders`

For full MySQL setup and exact SQL execution order, see:
- `monthly_revenue_analysis/sql/README.md`

---

## Installation

From the repository root:

pip install -r requirements.txt

## Reproducible Runs

### One-click main pipeline (recommended)

Command:
python monthly_revenue_analysis/run_all.py --save

What it does:
- Executes the full pipeline (Fig.01–Fig.11) in a fixed order
- Writes figures + metrics artifacts to disk

### Run a single script (example)

Command:
python monthly_revenue_analysis/scripts/analysis/fig01_smoothed_trend.py

### Run modeling & simulation modules

Commands:
python monthly_revenue_analysis/scripts/modeling/10_model_comparison_LR_RF.py
python monthly_revenue_analysis/scripts/modeling/11_monte_carlo_simulation.py

Note:
- The monthly panel covers a limited time span (roughly 2010–2011, ~24 monthly observations).
- The modeling focus is therefore on interpretability, time-consistent evaluation, and uncertainty quantification rather than high-capacity forecasting.

---

## Outputs

When running with --save, artifacts are written to:
- monthly_revenue_analysis/outputs/latest/figures/
- monthly_revenue_analysis/outputs/latest/metrics/

Behavior:
- If outputs/ does not exist, it is created automatically.
- These runtime artifacts are intended for reproduction and review and are typically excluded from version control.

---

## Advanced Experiments (Optional)

Location:
- monthly_revenue_analysis/experiments/

What’s included:
- Copula dependence sweep (dependence stress test)
- Bootstrap uncertainty quantification (parameter uncertainty intervals)
- Decision threshold loop (simple risk-constraint search)

Run an experiment (example):
python monthly_revenue_analysis/experiments/scripts/run_experiment.py --config monthly_revenue_analysis/experiments/configs/exp_copula_rho_sweep.yaml

Experiment outputs:
- monthly_revenue_analysis/experiments/outputs/<timestamp>_<experiment_name>/

Behavior:
- The output directory is created automatically if missing.

---

## Report

PDF:
monthly_revenue_analysis.pdf

---

## Author

Zhong Yuyang
Email: zhongyuyangm4@gmail.com

---

## License

MIT License
