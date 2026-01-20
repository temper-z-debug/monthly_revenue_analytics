USE retail_etl;

DROP TABLE IF EXISTS monthly_revenue;

CREATE TABLE monthly_revenue AS
SELECT
  DATE_FORMAT(InvoiceDT, '%Y-%m-01') AS 'year_month',
  ROUND(SUM(revenue), 2) AS total_revenue,
  COUNT(DISTINCT InvoiceNo) AS num_orders
FROM clean_online_retail
GROUP BY DATE_FORMAT(InvoiceDT, '%Y-%m-01')
ORDER BY 'year_month';

SELECT * FROM monthly_revenue ORDER BY 'year_month';
