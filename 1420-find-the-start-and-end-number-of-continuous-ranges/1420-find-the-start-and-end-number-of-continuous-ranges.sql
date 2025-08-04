
select  min(log_id) start_id,max(log_id) end_id from 
(select log_id, log_id- row_number() over(order by log_id) gid
from logs
order by log_id
) a
group by gid
order by start_id