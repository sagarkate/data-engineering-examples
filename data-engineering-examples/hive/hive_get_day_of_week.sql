
-- Fetch the number of the day of the week for current date.
-- This number ranges from 1 to 7.
-- 1 being 'Monday' and 7 being 'Sunday'

SELECT FROM_UNIXTIME(UNIX_TIMESTAMP(CURRENT_DATE(), 'yyyy-MM-dd'), 'u') AS day_of_the_week;

SELECT DATE_FORMAT(CURRENT_DATE, 'u') AS day_of_the_week;

SELECT EXTRACT(dayofweek from CURRENT_DATE);

-- You can replace CURRENT_DATE with any date type column 
-- or you could convert string to date and use that in place of CURRENT_DATE.
