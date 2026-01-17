# Monthly Revenue Analysis

This folder contains the full Python implementation for an end-to-end monthly revenue analytics project, including exploratory analysis, statistical diagnostics, predictive modeling, and Monte Carlo simulation.

The code in this directory is organized as a reproducible analytics pipeline, where each script corresponds to a specific analytical step and a figure in the final portfolio PDF.

---

## Project Overview

The goal of this project is to analyze monthly revenue dynamics using historical e-commerce data, with a focus on:

- Trend and seasonality detection  
- Revenue growth decomposition (orders vs. AOV)  
- Statistical relationship between revenue and order volume  
- Predictive modeling using regression and ensemble methods  
- Revenue uncertainty quantification via Monte Carlo simulation  

All analysis results are summarized visually in a portfolio-style PDF (Fig.01–Fig.11).

---

## Directory Structure

```
monthly_revenue_analysis/
│
├── analysis/              # Exploratory data analysis and statistical diagnostics
├── modelling/             # Predictive models and Monte Carlo simulation
├── utils/                 # Shared helper functions (data loading, plotting utilities)
├── figures/               # Final figures used in the PDF portfolio
├── data/
│   ├── raw/               # Raw source data (excluded from GitHub)
│   └── processed/         # Cleaned and aggregated data used by scripts
└── README.md              # This file
```

---

## Script-to-Figure Mapping

Each script is designed to be run independently and produces one main figure.

### Analysis Scripts

| Script | Output Figure | Description |
|--------|---------------|-------------|
| `01_smoothed_trend.py` | Fig. 01 | Smoothed revenue trend with peak identification |
| `02_yoy_revenue_by_month.py` | Fig. 02 | Month-aligned year-over-year seasonality |
| `03_dual_axis_revenue_orders.py` | Fig. 03 | Revenue vs. order volume comparison |
| `04_aov_trend.py` | Fig. 04 | Average Order Value (AOV) trend |
| `05_yoy_growth_rate.py` | Fig. 05 | Year-over-year revenue growth rate |
| `07_scatter_revenue_vs_orders.py` | Fig. 07 | Regression of orders vs. revenue |
| `09_boxplot_revenue_by_year.py` | Fig. 09 | Yearly revenue distribution and outliers |

### Modelling Scripts

| Script | Output Figure | Description |
|--------|---------------|-------------|
| `10_model_comparison_lr_rf.py` | Fig. 10 | Linear Regression vs Random Forest (holdout test) |
| `11_monte_carlo_simulation.py` | Fig. 11 | Monte Carlo simulation of revenue uncertainty |

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run analysis scripts (order not required)

```
python analysis/01_smoothed_trend.py
python analysis/02_yoy_revenue_by_month.py
python analysis/03_dual_axis_revenue_orders.py
python analysis/04_aov_trend.py
python analysis/05_yoy_growth_rate.py
python analysis/07_scatter_revenue_vs_orders.py
python analysis/09_boxplot_revenue_by_year.py
```

### 3. Run modeling and simulation

```
python modelling/10_model_comparison_lr_rf.py
python modelling/11_monte_carlo_simulation.py
```

---

## Reproducibility Notes

- Data loading is centralized via `utils/load_data.py`
- Randomness in modeling and simulation can be controlled using seeds
- All figures in `figures/` are generated directly from the scripts in this folder

---

## Intended Audience

This codebase is designed for:

- Data Science / Computing / Engineering program applications  
- Portfolio demonstration of analytics and modeling skills  
- Reproducible experimentation and future extension  
