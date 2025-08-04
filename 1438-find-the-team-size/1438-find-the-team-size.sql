select e.employee_id , ifnull(t.team_size,0) team_size from  employee e
left join 
(
select team_id,count(1) team_size
from employee
group by team_id) t on e.team_id=t.team_id