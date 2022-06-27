-- Convert string to date
SELECT TO_DATE(
    FROM_UNIXTIME(
        UNIX_TIMESTAMP(
            '12-05-2022 13:24:45', 
            'dd-MM-yyyy HH:mm:ss'))) AS converted_date
;
