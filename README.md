# Monthly Revenue Analytics

This repository contains a reproducible data analysis and modeling workflow for monthly revenue data.  
The objective is to characterize revenue dynamics, quantify underlying drivers, and evaluate predictive and stochastic models in a controlled, well-structured environment.

The codebase is modular, script-driven, and designed to support traceable experimentation rather than monolithic notebooks.  
All figures and statistics are generated directly from the scripts under `monthly_revenue_analysis/`.

---

## Key Methodology

- **Trend and seasonality diagnostics**  
  Smoothing, peak identification, and month-aligned YoY comparison to isolate cyclic structure.

- **Deterministic driver decomposition**  
  Revenue is analyzed as `Orders × AOV`, allowing separation between volume-driven and price-driven effects.

- **Predictive modeling**  
  Linear Regression and Random Forest models using lag features and month encodings.  
  Holdout evaluation is used instead of random shuffle to maintain time consistency.

- **Stochastic simulation**  
  Revenue uncertainty is modeled using a Normal distribution for orders and a Gamma distribution for AOV.  
  Monte Carlo draws enable estimation of downside risk and tail behavior.

- **Reproducibility**  
  Deterministic seeds, centralized data loading, and isolated scripts ensure consistent execution.

---

## Repository Structure

```
monthly_revenue_analysis/
│
├── analysis/              # Trend, seasonality, YoY, driver diagnostics
├── modelling/             # Predictive models and Monte Carlo simulation
├── utils/                 # Data loaders, plot styling, helper utilities
├── figures/               # Generated figures (Fig.01–Fig.11)
└── data/                  # Processed data (raw data excluded)
```

A more detailed mapping between scripts and output figures is provided in:

👉 `monthly_revenue_analysis/README.md`

---

## Running the Project

Setup:

```
pip install -r requirements.txt
```

Run any analysis module (example):

```
python analysis/01_smoothed_trend.py
```

Model comparison and simulation:

```
python modelling/10_model_comparison_lr_rf.py
python modelling/11_monte_carlo_simulation.py
```

Scripts display figures interactively and log intermediate results when relevant.

---

## Report

A consolidated document with the generated figures (Fig.01–Fig.11) is available at:

```
03.pdf
```

This document mirrors the output produced by the analysis and modeling scripts.

---

## Author

Zhong Yuyang  
GitHub: https://github.com/temper-z-debug

---

## License

MIT License.

