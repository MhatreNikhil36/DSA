# Write your MySQL query statement below
select player_id, max(streak) longest_streak from (
select player_id, sum( case when result='Win' then 1 else 0 end ) streak 
from(
select player_id  ,match_day  , result      ,
row_number() over (partition by  player_id order by match_day)-
row_number() over (partition by  player_id,result order by match_day) grp
from matches 
)  a
group by player_id,grp) t
group by player_id


