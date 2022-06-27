-- Below query is executed in BigQuery

-- Sample Input:
-- id,pid
-- a,b
-- b,c
-- d,e
-- f,g
-- g,h
-- i,j

-- Sample Output:
-- id,pid
-- a,b
-- b,c
-- f,g
-- g,h

-- SOLUTION#1:
WITH sample_cte AS (
  SELECT 'a' AS id, 'b' AS pid
  UNION ALL
  SELECT 'b' AS id, 'c' AS pid
  UNION ALL
  SELECT 'd' AS id, 'e' AS pid
  UNION ALL
  SELECT 'f' AS id, 'g' AS pid
  UNION ALL
  SELECT 'g' AS id, 'h' AS pid
  UNION ALL
  SELECT 'i' AS id, 'j' AS pid
)

, is_chained_cte AS (
SELECT
  id, pid,
  LAG(pid) OVER(ORDER BY id) AS prev_pid,
  LEAD(id) OVER(ORDER BY id) AS next_id,
  (id = LAG(pid) OVER(ORDER BY id) OR pid = LEAD(id) OVER(ORDER BY id)) AS is_chained
FROM sample_cte
)

SELECT

  id, pid

FROM is_chained_cte

WHERE 
  is_chained = TRUE
;

-- Execution Details:
-- Elapsed time: 157 ms
-- Slot time consumed: 15 ms
-- Bytes shuffled: 44 B
-- Bytes spilled to disk: 0 B

-- Stage0: Output - Records Read: 0 and Records Written: 4
-- Wait: 4 ms
-- Read: 0 ms
-- Compute: 3 ms
-- Write: 4 ms

-- If the data is small in size, above query would be most perfromant.
-- But Above Query would time out if the data is huge, 
-- since we are not specifiying partition by clause in window function.

-- SOLUTION#2:
WITH sample_cte AS (
  SELECT 'a' AS id, 'b' AS pid
  UNION ALL
  SELECT 'b' AS id, 'c' AS pid
  UNION ALL
  SELECT 'd' AS id, 'e' AS pid
  UNION ALL
  SELECT 'f' AS id, 'g' AS pid
  UNION ALL
  SELECT 'g' AS id, 'h' AS pid
  UNION ALL
  SELECT 'i' AS id, 'j' AS pid
)

SELECT
  s1.id,
  s1.pid
FROM sample_cte AS s1
JOIN sample_cte AS s2
  ON s1.pid = s2.id OR s1.id = s2.pid
;

-- Execution Details:
-- Elapsed time: 337 ms
-- Slot time consumed: 339 ms
-- Bytes shuffled: 188 B
-- Bytes spilled to disk: 0 B

-- Stage0: Input - Records Read: 0 and Records Written: 6
-- Wait: 1 ms
-- Read: 0 ms
-- Compute: 5 ms
-- Write: 138 ms

-- Stage1: Input - Records Read: 0 and Records Written: 6
-- Wait: 42 ms
-- Read: 0 ms
-- Compute: 4 ms
-- Write: 100 ms

-- Stage2: Output - Records Read: 12 and Records Written: 4
-- Wait: 2 ms
-- Read: 0 ms
-- Compute: 7 ms
-- Write: 6 ms

-- Above query would handle time-out issue.
-- But, it would be less performant as data increases due to multiple stages, 
-- OR condition in JOIN and shuffle operations.
-- If we look at stage2, it is using CROSS ALL WITH ALL join strategy
-- $1, $2
-- FROM __stage01_output
-- $10, $11
-- FROM __stage00_output
-- or(equal($141, $142), equal($140, $143))
-- $140 := $1, $141 := $2, $142 := $10, $143 := $11
-- CROSS ALL WITH ALL
-- $140, $141
-- TO __stage02_output

-- SOLUTION#3: Using ARRAY and UNNEST
WITH sample_cte AS (
  SELECT 'a' AS id, 'b' AS pid
  UNION ALL
  SELECT 'b' AS id, 'c' AS pid
  UNION ALL
  SELECT 'd' AS id, 'e' AS pid
  UNION ALL
  SELECT 'f' AS id, 'g' AS pid
  UNION ALL
  SELECT 'g' AS id, 'h' AS pid
  UNION ALL
  SELECT 'i' AS id, 'j' AS pid
)

, id_set_cte AS (
SELECT
  [STRUCT(s1.id,s1.pid), STRUCT(s2.id, s2.pid)] AS id_set
FROM sample_cte AS s1
JOIN sample_cte AS s2
  ON s1.pid = s2.id
)

SELECT
  id_row.id,
  id_row.pid
FROM id_set_cte
CROSS JOIN UNNEST(id_set) AS id_row
;

-- Execution Details:
-- Elapsed time: 387 ms
-- Slot time consumed: 307 ms
-- Bytes shuffled: 188 B
-- Bytes spilled to disk: 0 B

-- Stage0: Input - Records Read: 0 and Records Written: 6
-- Wait: 14 ms
-- Read: 0 ms
-- Compute: 7 ms
-- Write: 117 ms

-- Stage1: Input - Records Read: 0 and Records Written: 6
-- Wait: 47 ms
-- Read: 0 ms
-- Compute: 7 ms
-- Write: 116 ms

-- Stage2: Output - Records Read: 12 and Records Written: 4
-- Wait: 15 ms
-- Read: 0 ms
-- Compute: 8 ms
-- Write: 5 ms

-- If we look at stage2 execution details, it is using HASH JOIN ALL WITH ALL strategy
-- $20, $21
-- FROM __stage01_output
-- $30, $31
-- FROM __stage00_output
-- $1 := make_array($160, $162)
-- $2 := make_array($161, $163)
-- $160 := $20, $161 := $21, $162 := $30, $163 := $31
-- INNER HASH JOIN ALL WITH ALL ON $21 = $30
-- $10, $11
-- TO __stage02_output
