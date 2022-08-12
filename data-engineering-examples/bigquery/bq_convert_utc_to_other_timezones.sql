-- In BigQuery, CURRENT_TIMESTAMP() returns current timestamp in UTC.
-- TIMESTAMP data type stores data only in UTC.
-- If we need timestamp in any other timezone, we need to explicitly convert it.
-- We can perform the conversion using DATETIME() function.
-- But, it returns DATETIME object, not the TIMESTAMP. We need to keep this in mind.
-- DATETIME object provides us with only date and time component. It doesn't have timezone component with it.

SELECT
  CURRENT_TIMESTAMP() AS utc_ts,
  DATETIME(CURRENT_TIMESTAMP(), 'Asia/Kolkata') AS ist_datetime,
  DATETIME(CURRENT_TIMESTAMP(), 'America/Toronto') AS est_datetime,
  DATETIME(CURRENT_TIMESTAMP(), 'America/Los_Angeles') AS pst_datetime,
  DATETIME(CURRENT_TIMESTAMP(), 'Europe/Berlin') AS cet_datetime
;
