-- Below Query is executed in MySQL

-- Sample Input:
-- Team1    Team2   Winner
-- India	SL	    India
-- SL	    Aus	    Aus
-- SA	    ENG	    Eng
-- Eng	    NZ	    NZ
-- AUS	    India	INDIA

-- Output:
-- team_name    total_match_count   total_win_count total_loss_count
-- INDIA	    2	                2               0
-- SL	        2	                0	            2
-- SA	        1	                0	            1
-- ENG	        2	                1	            1
-- AUS	        2	                1	            1
-- NZ	        1	                1	            0

WITH matches_cte AS (
  SELECT
	UPPER(team1) AS team_name,
    UPPER(winner) AS winner
  FROM `sagar_mysql_practice`.practice2_matches
  
  UNION ALL
  
  SELECT
	UPPER(team2) AS team_name,
    UPPER(winner) AS winner
  FROM `sagar_mysql_practice`.practice2_matches
  ),
  
  winner_cte AS (
  SELECT
    UPPER(winner) AS team_name,
    COUNT(1) AS total_win_count
  FROM `sagar_mysql_practice`.practice2_matches
  GROUP BY UPPER(winner)
  ),
  
  total_matches_cte AS (
  SELECT
	team_name,
    COUNT(1) AS total_match_count
  FROM matches_cte
  GROUP BY team_name
  )
  
  SELECT
	tmc.team_name,
    tmc.total_match_count,
    COALESCE(wc.total_win_count, 0) AS total_win_count,
    (tmc.total_match_count - COALESCE(wc.total_win_count, 0)) AS total_loss_count
  FROM total_matches_cte AS tmc
  LEFT JOIN winner_cte AS wc
	ON tmc.team_name = wc.team_name
;