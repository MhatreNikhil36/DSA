# Write your MySQL query statement below
select p.player_id ,p.player_name,count(id)  grand_slams_count 
from
players p  join
(
select Wimbledon    id
from Championships
union all 
select Fr_open           id
from Championships
union all 
select us_open           id
from Championships
union all 
select au_open           id
from Championships
) a
on p.player_id=a.id
group by p.player_name

