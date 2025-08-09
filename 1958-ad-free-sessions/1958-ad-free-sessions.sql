# Write your MySQL query statement below
select p.session_id
from playback p
left  join ads a
on a.customer_id=p.customer_id
group by p.session_id
having sum(case  when a.timestamp    between p.start_time and p.end_time then 1 else  0 end)<1