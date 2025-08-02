# Write your MySQL query statement below
select u.name ,ifnull(r.distance,0) travelled_distance 
from users u left join 
(select user_id,sum(distance) distance from rides
group by user_id) r
on u.id=r.user_id
order by r.distance desc,u.name asc
