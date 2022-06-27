-- ** 1.Check if a specific string is in a given column ** --
SELECT
    CONTAINS_SUBSTR('JOHN SNOW|NED STARK', '|') AS does_it_contain_pipe
;

-- ** 2. Fetch Substring using index of a delimiter
SELECT
  SUBSTR('Programming in Scala: Martin Odersky', 1, INSTR('Programming in Scala: Martin Odersky', ':', 1)-1) AS book_title
;

-- ** 3. Concatenate using concatenation operator '||'
SELECT 'BigQuery' || ' ' || 'Guide' AS name
;
