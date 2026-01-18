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

`monthly_revenue_analysis/README.md`

## Data Source and Data Cleaning Pipeline

### Data Source

This project is based on the Online Retail II transactional dataset, originally published by the UCI Machine Learning Repository:

Chen, D. (2015). Online Retail II Data Set.
https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains all transactions occurring between 01/12/2009 and 09/12/2011 for a UK-based online retail company. Each record corresponds to a single line item in a customer order.

Raw data fields include:
- InvoiceNo: Transaction identifier
- StockCode: Product identifier
- Description: Product description
- Quantity: Number of units purchased (can be negative for returns)
- InvoiceDate: Transaction timestamp
- UnitPrice: Price per unit
- CustomerID: Anonymized customer identifier
- Country: Customer country

NOTE:
Due to licensing and file size considerations, the raw dataset (online_retail_II.csv) is not included in this repository.
The cleaned and aggregated dataset used for analysis is provided in:
data/processed/monthly_revenue.csv


### Data Cleaning and Preprocessing

The raw transaction-level data undergoes a structured ETL (Extract–Transform–Load) process implemented via SQL scripts located in the sql/ directory.
The objective is to produce a clean, interpretable monthly revenue time series suitable for descriptive analysis, trend decomposition, and forecasting.


Step 1: Raw Data Ingestion

- Raw CSV data is imported into MySQL using sql/00_setup.sql
- All fields are ingested without transformation to preserve original information


Step 2: Transaction Filtering

The following filters are applied to remove invalid or non-economic transactions:

- Cancelled invoices removed
  Transactions with InvoiceNo starting with 'C' are excluded.

- Returns and corrections removed
  Records with Quantity ≤ 0 are excluded.

- Invalid pricing removed
  Records with UnitPrice ≤ 0 are excluded.

- Missing customer identifiers removed
  Rows with CustomerID IS NULL are excluded.

These rules follow standard practices in retail transaction analysis and ensure that revenue values reflect completed sales only.


Step 3: Revenue Computation

For each valid transaction line, revenue is computed as:

Revenue = Quantity × UnitPrice

The revenue is calculated at the line-item level and stored as a derived column during transformation.


Step 4: Temporal Aggregation

- Transaction timestamps are converted to Year–Month format (YYYYMM).
- Revenue is aggregated at the monthly level:

Monthly Revenue = Σ (Quantity × UnitPrice)
Monthly Orders  = COUNT(DISTINCT InvoiceNo)

This aggregation produces a monthly panel suitable for time-series analysis while smoothing high-frequency transactional noise.


Step 5: Validation Checks

Basic data integrity and sanity checks are performed in sql/04_validation_checks.sql, including:
- Verification of continuous monthly coverage
- Detection of zero or negative aggregated revenue
- Consistency checks of summary statistics


### Final Analytical Dataset

The final cleaned dataset is stored at:

data/processed/monthly_revenue.csv

with the following schema:

- year_month: Year–month identifier (YYYYMM)
- total_revenue: Total revenue in that month
- num_orders: Number of unique orders in that month

This dataset serves as the single source of truth for all subsequent Python-based analyses and visualizations
(analysis/01_*.py through analysis/11_*.py).


### Reproducibility Note

To fully reproduce the processed dataset from raw data:

1. Download Online Retail II from the UCI repository
2. Import the raw CSV into MySQL
3. Execute the SQL pipeline:

mysql -u <user> -p < sql/etl_pipeline.sql

4. Export the resulting monthly table to data/processed/monthly_revenue.csv

Alternatively, users may directly run the Python analysis scripts using the provided processed dataset.


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
Email: <zhongyuyangm4@gmail.com> 

---

## License

MIT License.

