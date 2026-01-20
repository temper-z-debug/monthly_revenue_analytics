# Monthly Revenue Analytics

This repository presents a reproducible, script-driven workflow for analyzing **monthly revenue dynamics** and evaluating both **predictive** and **simulation-based** approaches. I built it as a portfolio project with a focus on: (i) explicit assumptions, (ii) time-consistent evaluation, and (iii) artifacts that can be regenerated end-to-end.

The core pipeline lives under `monthly_revenue_analysis/`. Optional research-style extensions (config-driven experiments) live under `monthly_revenue_analysis/experiments/`.

---

## What you can review quickly

- **Preview figures (committed):** `monthly_revenue_analysis/figures/`  
  Selected figures are committed for fast GitHub browsing.

- **Reproducible run outputs:** `monthly_revenue_analysis/outputs/latest/`  
  Running the one-click pipeline writes:
  - `outputs/latest/figures/` (generated figures)
  - `outputs/latest/metrics/` (CSV/JSON summaries and model outputs)

- **Report (narrative + figures):** `monthly_revenue_analysis.pdf`

---

## Project questions

1) How does revenue evolve over time (trend and seasonality)?  
2) Are changes driven by **Orders** or **AOV** (basket size)?  
3) How well can we predict revenue under **time-consistent evaluation** (no shuffle)?  
4) How uncertain are outcomes, and what do tail behaviors look like under simulation?

---

## Methodology overview

- **Trend and seasonality diagnostics**  
  Smoothing, peak identification, month-aligned YoY views, rolling summaries, and distribution checks.

- **Driver decomposition**  
  Interpretable factorization with `Revenue = Orders × AOV` to separate volume-driven vs. basket-driven effects.

- **Predictive modeling (time-consistent evaluation)**  
  Lag features + month encodings; chronological holdout split to avoid temporal leakage.

- **Stochastic simulation (uncertainty and tail behavior)**  
  Monte Carlo simulation to quantify uncertainty and summarize tail risk.

- **Reproducibility**  
  Centralized data loading, deterministic seeds, and standardized artifact writing.

---

## Repository structure

```text
monthly_revenue_analysis/
│
├── data/                  # Processed data (raw data excluded)
├── utils/                 # Data loaders, plot styling, helper utilities
├── scripts/               # Main pipeline scripts
│   ├── analysis/          # Fig.01–Fig.09 (trend/seasonality/driver diagnostics)
│   └── modeling/          # Fig.10–Fig.11 (models + simulation)
├── sql/                   # SQL ETL pipeline (raw transactions → cleaned monthly panel) + validation checks
├── experiments/           # Config-driven experiments (copula stress test, bootstrap UQ, decision threshold)
├── figures/               # Selected preview figures committed for GitHub browsing
└── run_all.py             # One-click runner for the main pipeline
```

A more detailed mapping between scripts and output figures is provided in:  
`monthly_revenue_analysis/README.md`

---

## Data source

This project is based on the **Online Retail II** transactional dataset (UCI Machine Learning Repository):

Chen, D. (2015). Online Retail II Data Set.  
https://archive.ics.uci.edu/dataset/352/online+retail

The raw transaction-level CSV is not included in this repository (licensing / size considerations). This repo includes the cleaned and aggregated monthly dataset used by all Python scripts:

- `monthly_revenue_analysis/data/processed/monthly_revenue.csv`

---

## Data cleaning and ETL (SQL)

Transaction-level records are transformed into a monthly panel using SQL scripts in `monthly_revenue_analysis/sql/`. The goal is to remove non-economic entries and produce a clean, interpretable time series.

**Step 1 — Raw ingestion**
- Import the raw CSV into MySQL staging tables (see `sql/00_setup.sql` and `sql/01_load_raw_online_retail.sql`).
- Ingest without transformation to preserve original fields.

**Step 2 — Transaction filtering**
Remove invalid or non-economic records:
- Cancelled invoices removed: exclude `InvoiceNo` starting with `'C'`
- Returns/corrections removed: exclude `Quantity <= 0`
- Invalid pricing removed: exclude `UnitPrice <= 0`
- Missing customer identifiers removed: exclude `CustomerID IS NULL`

**Step 3 — Revenue computation**
- Compute line-item revenue: `Revenue = Quantity × UnitPrice`

**Step 4 — Monthly aggregation**
- Convert `InvoiceDate` to `YYYYMM`
- Aggregate:
  - `total_revenue = Σ Revenue`
  - `num_orders = COUNT(DISTINCT InvoiceNo)`

**Step 5 — Validation checks**
- Sanity checks are implemented in `sql/04_validation_checks.sql` (coverage checks, negative/zero revenue detection, summary consistency).

For exact MySQL setup and execution order, see:  
- `monthly_revenue_analysis/sql/README.md`

---

## Reproducible runs

### Install dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

### One-click main pipeline (recommended)

```bash
python monthly_revenue_analysis/run_all.py --save
```

This executes the full pipeline (Fig.01–Fig.11) in a fixed order and writes artifacts to disk.

### Run a single script (example)

```bash
python monthly_revenue_analysis/scripts/analysis/fig01_smoothed_trend.py
```

### Run modeling & simulation modules

```bash
python monthly_revenue_analysis/scripts/modeling/10_model_comparison_LR_RF.py
python monthly_revenue_analysis/scripts/modeling/11_monte_carlo_simulation.py
```

**Note on dataset size**  
The monthly panel covers a limited time span (roughly 2010–2011, ~24 monthly observations). The modeling focus is therefore on interpretability, time-consistent evaluation, and uncertainty quantification rather than high-capacity forecasting.

---

## Outputs

When running with `--save`, artifacts are written to:
- `monthly_revenue_analysis/outputs/latest/figures/`
- `monthly_revenue_analysis/outputs/latest/metrics/`

If `outputs/` does not exist, it is created automatically. These runtime artifacts are generated for reproduction and review and are typically excluded from version control.

**Recommended version control practice**
- Commit: `monthly_revenue_analysis/figures/` (selected previews)
- Do not commit: `monthly_revenue_analysis/outputs/` and `monthly_revenue_analysis/experiments/outputs/` (runtime artifacts)

---

## Advanced experiments (optional)

The `monthly_revenue_analysis/experiments/` folder contains config-driven, research-style extensions:
- Copula dependence sweep: counterfactual dependence stress test (holding fitted marginals fixed while varying dependence)
- Bootstrap uncertainty quantification: parameter uncertainty intervals for key metrics
- Decision threshold loop: a simple risk-constraint-style search using empirical simulation outputs

Run an experiment (example):

```bash
python monthly_revenue_analysis/experiments/scripts/run_experiment.py --config monthly_revenue_analysis/experiments/configs/exp_copula_rho_sweep.yaml
```

Experiment outputs are written to:
- `monthly_revenue_analysis/experiments/outputs/<timestamp>_<experiment_name>/`

The output directory is created automatically if missing.

---

## Report

A consolidated PDF report (figures + narrative) is available at:
- `monthly_revenue_analysis.pdf`

---

## Author

Zhong Yuyang  
Email: zhongyuyangm4@gmail.com

---

## License

MIT License
