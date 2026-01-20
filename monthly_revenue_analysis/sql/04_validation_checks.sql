USE retail_etl;

-- Row counts
SELECT 'staging_rows' AS metric, COUNT(*) AS value FROM stg_online_retail
UNION ALL
SELECT 'clean_rows', COUNT(*) FROM clean_online_retail
UNION ALL
SELECT 'months', COUNT(*) FROM monthly_revenue;

-- Cancelled invoice share in staging
SELECT
  ROUND(100.0 * SUM(CASE WHEN Invoice LIKE 'C%' THEN 1 ELSE 0 END) / COUNT(*), 4) AS pct_cancelled
FROM stg_online_retail
WHERE Invoice IS NOT NULL;

-- Non-positive qty/price counts in staging
SELECT
  SUM(CASE WHEN Quantity IS NULL OR Quantity <= 0 THEN 1 ELSE 0 END) AS bad_qty_rows,
  SUM(CASE WHEN Price IS NULL OR Price <= 0 THEN 1 ELSE 0 END) AS bad_price_rows
FROM stg_online_retail;

-- Monthly totals sanity
SELECT
  MIN('year_month') AS min_month,
  MAX('year_month') AS max_month,
  ROUND(SUM(total_revenue), 2) AS revenue_sum,
  SUM(num_orders) AS order_sum
FROM monthly_revenue;
