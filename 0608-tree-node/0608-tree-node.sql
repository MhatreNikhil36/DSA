# Write your MySQL query statement below
with parents as (
    select distinct p_id id from tree
    where p_id is not null
)
select id, case when  p_id is null then 'Root'
when id not in (select id from parents) then 'Leaf'
else 'Inner' end  as type 
from tree