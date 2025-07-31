# Write your MySQL query statement below
-- count of the canceled  trip  with  id  make  sure  id not in  banned 

with  banned as (
select users_id as id from users where  banned like 'Yes' 
)
-- ,
select  request_at as Day,round(nc/c,2) as  'Cancellation Rate' from (
select request_at,sum(nc) nc,sum(c) c from
(
select  request_at, 1  as c,
case when status not like 'completed' then 1  else 0 end as nc 
from trips
where client_id  not in (select id from banned)  and  driver_id   not in (select id from banned)   and request_at between "2013-10-01" and "2013-10-03"
) as TripCount
group by  request_at) agg 