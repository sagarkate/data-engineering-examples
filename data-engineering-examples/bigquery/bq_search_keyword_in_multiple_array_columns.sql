-- Sample Data
-- app1	            app2
-- [app,app1]	    []
-- []	            [app]
-- [app1]	        [app]
-- []	            []

WITH arr_cte AS (
  SELECT array(SELECT 'app' UNION ALL SELECT 'app1') AS app1, [] AS app2
  UNION ALL
  SELECT [] AS app1, ['app'] AS app2
  UNION ALL
  SELECT ['app1'] AS app1, ['app'] AS app2
  UNION ALL
  SELECT [] AS app1, [] AS app2
)

SELECT * FROM arr_cte
WHERE CONTAINS_SUBSTR(ARRAY_TO_STRING(app1, '_'), 'app') OR CONTAINS_SUBSTR(ARRAY_TO_STRING(app2, '_'), 'app')
;

WITH arr_cte AS (
  SELECT array(SELECT 'app' UNION ALL SELECT 'app1') AS app1, [] AS app2
  UNION ALL
  SELECT [] AS app1, ['app'] AS app2
  UNION ALL
  SELECT ['app1'] AS app1, ['app'] AS app2
  UNION ALL
  SELECT [] AS app1, [] AS app2
)

SELECT * FROM arr_cte
WHERE CONTAINS_SUBSTR(ARRAY_CONCAT(app1, app2), 'app')
;

WITH arr_cte AS (
  SELECT array(SELECT 'app' UNION ALL SELECT 'app1') AS app1, [] AS app2
  UNION ALL
  SELECT [] AS app1, ['app'] AS app2
  UNION ALL
  SELECT ['app1'] AS app1, ['app'] AS app2
  UNION ALL
  SELECT [] AS app1, [] AS app2
)

SELECT * FROM arr_cte
WHERE 'app' IN UNNEST(ARRAY_CONCAT(app1, app2)) -- this is the best solution
;
