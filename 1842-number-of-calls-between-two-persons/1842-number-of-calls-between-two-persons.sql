select distinct 
case  when ifnull(total_duration1,0)> ifnull(total_duration2,0) then a.person1  else b.person1 end as person1 ,
case when ifnull(total_duration1,0)> ifnull(total_duration2,0) then a.person2  else b.person2 end as person2 ,
ifnull(c1,0)+ifnull(c2,0) as call_count,
ifnull(total_duration1 ,0)+ifnull(total_duration2 ,0) as total_duration
from
(select from_id person1, to_id person2 , count(1)c1, sum(duration) total_duration1
from calls
group by person1,person2) a
left join 
(select from_id person1, to_id person2 , count(1)c2, sum(duration) total_duration2
from calls
group by person1,person2
) b on a.person1=b.person2
 and a.person2=b.person1