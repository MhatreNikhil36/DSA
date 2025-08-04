# Write your MySQL query statement below
select player_id,device_id from (
select player_id,device_id ,row_number() over(partition by player_id order by event_date asc) rn
from activity
) a
where rn=1