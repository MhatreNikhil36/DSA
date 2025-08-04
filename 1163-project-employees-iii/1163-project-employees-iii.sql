select project_id,employee_id from (
select p.project_id,e.employee_id,rank() over( partition by p.project_id order by experience_years desc) rn
from employee e
 join project p on e.employee_id=p.employee_id) master where rn=1