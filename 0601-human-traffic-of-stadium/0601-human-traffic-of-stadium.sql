# Write your MySQL query statement below
-- posible  postions of  valid  record is  
-- 1**
-- *1*
-- **1
-- if any of these  three scheck work  then  flad that  record  to  be included 
WITH windowed AS (
  SELECT 
    id,
    visit_date,
    people,
    LAG(people, 2) OVER (ORDER BY id) AS prev2,
    LAG(people, 1) OVER (ORDER BY id) AS prev1,
    LEAD(people, 1) OVER (ORDER BY id) AS next1,
    LEAD(people, 2) OVER (ORDER BY id) AS next2
  FROM stadium
)
SELECT 
  id, 
  visit_date, 
  people
FROM windowed
WHERE 
  (prev2 >= 100 AND prev1 >= 100 AND people >= 100)
  OR (prev1 >= 100 AND people >= 100 AND next1 >= 100)
  OR (people >= 100 AND next1 >= 100 AND next2 >= 100);



