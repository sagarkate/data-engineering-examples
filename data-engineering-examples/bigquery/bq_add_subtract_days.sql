-- Add or Subtract Days from a current date or any date column

SELECT
  CURRENT_DATE() AS current_date,
  DATE_ADD(CURRENT_DATE(), INTERVAL 7 DAY) AS next_week_date,
  DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY) AS previous_week_date
;