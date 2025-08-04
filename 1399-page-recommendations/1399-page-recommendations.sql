# Write your MySQL query statement below
select distinct l.page_id recommended_page 
from
( select case when user1_id=1 then user2_id      
when user2_id=1 then user1_id  else null end as fid
from friendship) f
left join     
likes l on f.fid=l.user_id
where l.page_id not in  (select page_id from likes where user_id=1) and l.page_id is not null