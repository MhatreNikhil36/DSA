WITH combined_calls AS (
  SELECT caller_id AS id, duration FROM calls
  UNION ALL
  SELECT callee_id AS id, duration FROM calls
),
joined_data AS (
  SELECT 
    i.name AS country,
    c.duration
  FROM combined_calls c
  LEFT JOIN Person p ON p.id = c.id
  LEFT JOIN Country i ON SUBSTRING(p.phone_number, 1, 3) = i.country_code
),
country_avg AS (
  SELECT 
    country,
    AVG(duration) AS country_avg
  FROM joined_data
  GROUP BY country
),
global_avg AS (
  SELECT AVG(duration) AS global_avg FROM joined_data
)
SELECT 
  c.country
FROM 
  country_avg c
  CROSS JOIN global_avg g
WHERE 
  c.country_avg > g.global_avg;
