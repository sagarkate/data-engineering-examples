-- We can use EXTRACT() function to fetch various date/time components from 
-- current_timestamp(), current_date() or any date/timestamp column.
-- NOTE: DAYOFWEEK - 1 means Sunday and 7 means Saturday.

SELECT 
  EXTRACT(YEAR FROM CURRENT_TIMESTAMP()) AS year,
  EXTRACT(MONTH FROM CURRENT_TIMESTAMP()) AS month,
  EXTRACT(WEEK FROM CURRENT_TIMESTAMP()) AS week,
  EXTRACT(DAY FROM CURRENT_TIMESTAMP()) AS day_of_month,
  EXTRACT(DAYOFWEEK FROM CURRENT_TIMESTAMP()) AS day_of_week,
  EXTRACT(HOUR FROM CURRENT_TIMESTAMP()) AS hour,
  EXTRACT(MINUTE FROM CURRENT_TIMESTAMP()) AS minute,
  EXTRACT(SECOND FROM CURRENT_TIMESTAMP()) AS seconds,
;

SELECT 
  EXTRACT(YEAR FROM CURRENT_DATE()) AS year,
  EXTRACT(MONTH FROM CURRENT_DATE()) AS month,
  EXTRACT(WEEK FROM CURRENT_DATE()) AS week,
  EXTRACT(DAY FROM CURRENT_DATE()) AS day_of_month,
  EXTRACT(DAYOFWEEK FROM CURRENT_DATE()) AS day_of_week
;