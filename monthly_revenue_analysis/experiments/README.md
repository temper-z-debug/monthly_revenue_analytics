# Advanced Experiments (MSMS-aligned)

This folder contains research-style counterfactual experiments that extend the core monthly revenue pipeline
(analysis/ + modelling/) with controlled stress tests, uncertainty quantification, and decision-oriented risk constraints.

All experiments are config-driven (YAML) and executed via a single runner script:
experiments/scripts/run_experiment.py

Outputs are NOT committed to Git. They are generated at runtime under:
monthly_revenue_analysis/outputs/experiments/<timestamp>_<experiment_name>/

-------------------------------------------------------------------------------

Folder Structure

experiments/
├── configs/                  # YAML configs (single source of truth)
│   ├── exp_bootstrap_uq.yaml
│   ├── exp_copula_rho_sweep.yaml
│   ├── exp_decision_threshold.yaml
│   └── seeds.yaml
├── scripts/
│   └── run_experiment.py     # unified runner: config -> run -> outputs
├── src/
│   ├── explain/              # optional explanatory helpers (if used)
│   └── sim/                  # reusable experiment logic (copula, metrics, utils)
│       ├── copula.py
│       ├── distributions.py
│       ├── experiment.py
│       ├── metrics.py
│       └── utils.py
└── README.md

-------------------------------------------------------------------------------

Quick Start

From the project root monthly_revenue_analysis/:

1) Install dependencies:
pip install -r ../requirements.txt

2) Run an experiment (example: copula sweep):
python experiments/scripts/run_experiment.py experiments/configs/exp_copula_rho_sweep.yaml

-------------------------------------------------------------------------------

Experiments

1) Copula Dependence Sweep (Counterfactual Dependence Stress Test)

Goal:
- Keep fitted marginals fixed (Orders, AOV) while varying only the dependence structure.
- Quantify how correlation affects tail risk (e.g., VaR/CVaR) and downside probability.

Config:
experiments/configs/exp_copula_rho_sweep.yaml

Run:
python experiments/scripts/run_experiment.py experiments/configs/exp_copula_rho_sweep.yaml

2) Bootstrap UQ (Parameter Uncertainty Quantification)

Goal:
- Estimate uncertainty bands of fitted parameters and derived risk metrics via bootstrap resampling.
- Provide confidence intervals for key quantities (e.g., mean revenue, VaR/CVaR).

Config:
experiments/configs/exp_bootstrap_uq.yaml

Run:
python experiments/scripts/run_experiment.py experiments/configs/exp_bootstrap_uq.yaml

3) Risk Constraint Threshold (Decision Loop via Bisection)

Goal:
- Solve a simple risk-control decision problem:
  find the minimum threshold / policy parameter such that a risk constraint is satisfied.
- Demonstrates a decision-oriented loop, not only descriptive modeling.

Config:
experiments/configs/exp_decision_threshold.yaml

Run:
python experiments/scripts/run_experiment.py experiments/configs/exp_decision_threshold.yaml

-------------------------------------------------------------------------------

Outputs and Version Control Policy

All experiment runs write artifacts under the project-local directory:

experiments/outputs/<timestamp>_<experiment_name>/

The output directory is created automatically at runtime (if it does not exist).
Typical artifacts include:
- results.csv
- metadata.json
- one or more figures (*.png)

These outputs are generated artifacts and should NOT be committed to Git.
Recommended .gitignore entry:

experiments/outputs/

-------------------------------------------------------------------------------

Notes for Reviewers

These experiments are designed to demonstrate:
- counterfactual reasoning (vary dependence while fixing marginals),
- uncertainty quantification beyond point estimates,
- decision-ready risk constraints (not just forecasting accuracy).
