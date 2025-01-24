# Write your MySQL query statement below
-- with acp as (select accepter_id id,count(requester_id ) num from RequestAccepted 
-- group by accepter_id),
-- req as (select requester_id id,count(accepter_id ) num from RequestAccepted 
-- group by requester_id)
-- select id, sum(num) num  from (
--     select * from acp
-- union all 
-- select * from req) a
-- group  by id order by num desc limit 1


select id , count(id) as num
from(
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted) as total
group by id
order by count(id) desc
limit 1;
