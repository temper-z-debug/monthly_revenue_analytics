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
    ├── monthly_revenue.csv
    └── data_quality_report.txt
```

---

## 1. Raw Data (`data/raw/`)

Raw invoice-level data is **not included** in the repository due to licensing restrictions and file size constraints.

The expected file is:

- `online_retail_II.csv`  
  A transactional dataset containing the following typical fields:

  - Invoice / InvoiceNo  
  - StockCode  
  - Description  
  - Quantity  
  - InvoiceDate  
  - UnitPrice / Price  
  - CustomerID  
  - Country  

This file must be placed manually into:

```
data/raw/online_retail_II.csv
```

---

## 2. Processed Data (`data/processed/`)

This directory contains all **cleaned and aggregated outputs** produced by:

- `data/make_dataset.py`
- or the SQL pipeline under `sql/`

### Files generated:

#### `monthly_revenue.csv`
Monthly aggregated dataset containing:

| column         | description                             |
|----------------|-----------------------------------------|
| year_month     | First day of the month (YYYY-MM-01)     |
| total_revenue  | Sum(Quantity × UnitPrice)               |
| num_orders     | Distinct invoice count                  |

#### `data_quality_report.txt`
A diagnostic report summarizing:

- missing values  
- negative quantities  
- invalid timestamps  
- customer ID anomalies  
- duplicate invoice rows  

---

## 3. Reproducibility Workflow

You may rebuild processed data using either method:

### Option A — Python ETL
```
python data/make_dataset.py \
    --raw data/raw/online_retail_II.csv \
    --out data/processed/monthly_revenue.csv \
    --report data/processed/data_quality_report.txt
```

### Option B — SQL Pipeline
Run the scripts under:

```
sql/00_setup.sql
sql/01_load_raw_online_retail.sql
sql/02_clean_transform.sql
sql/03_monthly_aggregation.sql
sql/04_validation_checks.sql
```

---

## 4. Notes

- Raw datasets are excluded via `.gitignore`.
- All figures in the report (Fig.01–Fig.11) are generated from `processed/`.
- SQL and Python pipelines are fully consistent and generate identical monthly revenue outputs.

