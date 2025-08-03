select  event_day day,emp_id,sum(out_time-in_time) total_time  
from employees
group by  emp_id, event_day
