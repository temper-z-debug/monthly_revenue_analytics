# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.

# SQL ETL (MySQL) — Online Retail II → Monthly Revenue

This directory contains a minimal, reproducible MySQL ETL pipeline that transforms raw invoice-level
transactions (`online_retail_II.csv`) into a monthly dataset used by the Python modelling scripts.

## Outputs
The final table matches the schema used in the Python pipeline:

- `year_month` (YYYY-MM-01)
- `total_revenue`
- `num_orders`

## Script Order

1. `00_setup.sql`  
   Creates database `retail_etl`.

2. `01_load_raw.sql`  
   Loads the raw CSV into `stg_online_retail`.  
   **You must update the `LOAD DATA LOCAL INFILE` path**.

3. `02_clean_transform.sql`  
   Applies deterministic cleaning rules and creates `clean_online_retail`.

4. `03_monthly_aggregation.sql`  
   Aggregates to `monthly_revenue`.

5. `04_validation_checks.sql`  
   Sanity checks for reproducibility and data quality.

## Notes
- Raw data is not committed to GitHub.
- Country filter defaults to `United Kingdom` to match the Python build script’s default behaviour.
