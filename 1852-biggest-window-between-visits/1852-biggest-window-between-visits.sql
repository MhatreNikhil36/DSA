select user_id,max(win) biggest_window from (
select user_id, datediff(ifnull(lead(visit_date) over(partition by user_id order by visit_date),date('2021-1-1')), visit_date)  win
from   UserVisits) a
group by user_id