# Write your MySQL query statement below
-- posible  postions of  valid  record is  
-- 1**
-- *1*
-- **1
-- if any of these  three scheck work  then  flad that  record  to  be included 

with pre as (
SELECT 
  id,visit_date ,
  LAG(people, 2, 0)  OVER (ORDER BY id) AS prev2,
  LAG(people, 1, 0)  OVER (ORDER BY id) AS prev1,
  people AS current,
  LEAD(people, 1, 0) OVER (ORDER BY id) AS next1,
  LEAD(people, 2, 0)  OVER (ORDER BY id) AS next2
FROM 
  stadium)
select id,visit_date,people from(
select id,visit_date ,current people, case when prev2>=100 and prev1>=100 and current>=100 then 1 
when prev1>=100 and next1>=100 and current>=100 then 1
when next2>=100 and next1>=100 and current>=100 then 1
else 0 end as include
from pre ) major
where include=1


