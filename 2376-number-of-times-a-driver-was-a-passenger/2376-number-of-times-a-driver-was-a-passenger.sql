# Write your MySQL query statement below
with drivers as (
select distinct driver_id  from rides
)
select d.driver_id, count(b.ride_id) cnt 
from drivers d
left join rides b on d.driver_id=b.passenger_id
group by 1 
 