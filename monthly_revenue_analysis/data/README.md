# Data Directory Documentation

This directory contains the datasets used in the **Monthly Revenue Analytics** project.

To maintain reproducibility and engineering clarity, the data pipeline follows a structured:

**raw → staging → cleaned → aggregated**

workflow.

---

## Directory Structure

```
data/
├── raw/               # Original invoice-level dataset (excluded from GitHub)
└── processed/         # Cleaned and aggregated monthly revenue data
    └── monthly_revenue.csv
```

---

## 1. Raw Data (`data/raw/`)

Raw invoice-level data is **not included** in the repository due to licensing restrictions and file size constraints.

The expected input file is:

- `online_retail_II.csv`  
  An invoice-level e-commerce dataset containing fields such as:

  - Invoice / InvoiceNo  
  - StockCode  
  - Description  
  - Quantity  
  - InvoiceDate  
  - UnitPrice / Price  
  - CustomerID  
  - Country  

For local execution, the raw dataset should be placed at:

```
data/raw/online_retail_II.csv
```

This raw data is not consumed directly by analysis scripts.

---

## 2. Data Cleaning and Aggregation

Data preprocessing is performed **before analysis**, using a deterministic ETL workflow implemented in SQL and Python.

### SQL-based ETL

Invoice-level data is ingested, validated, cleaned, and aggregated using MySQL scripts located in the `sql/` directory:

- removal of cancelled invoices and invalid quantities/prices  
- timestamp parsing and normalization  
- country-level filtering  
- aggregation from invoice-level to monthly metrics  

The final output of the SQL pipeline is a monthly revenue table consistent with the Python analysis interface.

### Python-based Processing

All Python analysis and modeling scripts load data exclusively from:

```
data/processed/monthly_revenue.csv
```

via the centralized loader in:

```
utils/load_data.py
```

This guarantees consistent preprocessing across all experiments.

---

## 3. Processed Data (`data/processed/`)

### `monthly_revenue.csv`

The final, analysis-ready dataset containing:

| column         | description                             |
|----------------|-----------------------------------------|
| year_month     | First day of the month (YYYY-MM-01)     |
| total_revenue  | Monthly total revenue                   |
| num_orders     | Distinct number of invoices             |

This file is version-controlled and serves as the single source of truth for all figures and models.

---

## 4. Reproducibility Notes

- Raw data is excluded from version control.
- Cleaning logic is explicit and reproducible via SQL and Python scripts.
- All figures (Fig.01–Fig.11) are generated solely from `monthly_revenue.csv`.


