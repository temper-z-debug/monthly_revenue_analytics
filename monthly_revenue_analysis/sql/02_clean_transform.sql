USE retail_etl;

DROP TABLE IF EXISTS clean_online_retail;

CREATE TABLE clean_online_retail AS
SELECT
  Invoice AS InvoiceNo,
  StockCode,
  Description,
  CAST(Quantity AS SIGNED) AS Quantity,
  STR_TO_DATE(InvoiceDate, '%Y-%m-%d %H:%i:%s') AS InvoiceDT,
  CAST(Price AS DECIMAL(12,4)) AS UnitPrice,
  NULLIF(CustomerID, '') AS CustomerID,
  Country,
  (CAST(Quantity AS SIGNED) * CAST(Price AS DECIMAL(12,4))) AS revenue
FROM stg_online_retail
WHERE
  Invoice IS NOT NULL
  AND InvoiceDate IS NOT NULL
  AND STR_TO_DATE(InvoiceDate, '%Y-%m-%d %H:%i:%s') IS NOT NULL
  AND Quantity IS NOT NULL
  AND Price IS NOT NULL
  AND CAST(Quantity AS SIGNED) > 0
  AND CAST(Price AS DECIMAL(12,4)) > 0
  AND Invoice NOT LIKE 'C%'          -- cancelled invoices
  -- Optional country filter (uncomment if you want to match your Python default)
  AND Country = 'United Kingdom';

-- Optional: remove duplicates by keeping distinct rows
-- (If your data has exact duplicates, this removes them.)
CREATE TABLE clean_online_retail_dedup AS
SELECT DISTINCT * FROM clean_online_retail;

DROP TABLE clean_online_retail;
RENAME TABLE clean_online_retail_dedup TO clean_online_retail;

-- Indexes for speed (optional but recommended)
ALTER TABLE clean_online_retail
  ADD INDEX idx_invoice_dt (InvoiceDT),
  ADD INDEX idx_invoice (InvoiceNo);
