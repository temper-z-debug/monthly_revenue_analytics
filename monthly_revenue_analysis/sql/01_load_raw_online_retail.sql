USE retail_etl;

DROP TABLE IF EXISTS stg_online_retail;

CREATE TABLE stg_online_retail (
  Invoice      VARCHAR(50),
  StockCode    VARCHAR(50),
  Description  TEXT,
  Quantity     INT,
  InvoiceDate  VARCHAR(50),
  Price        DECIMAL(12, 4),
  CustomerID   VARCHAR(50),
  Country      VARCHAR(100)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/online_retail_II.csv'
INTO TABLE stg_online_retail
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@Invoice, @StockCode, @Description, @Quantity, @InvoiceDate, @Price, @CustomerID, @Country)
SET
  Invoice     = NULLIF(@Invoice, ''),
  StockCode   = NULLIF(@StockCode, ''),
  Description = NULLIF(@Description, ''),
  Quantity    = NULLIF(@Quantity, ''),
  InvoiceDate = NULLIF(@InvoiceDate, ''),
  Price       = NULLIF(@Price, ''),
  CustomerID  = NULLIF(@CustomerID, ''),
  Country     = NULLIF(@Country, '');

