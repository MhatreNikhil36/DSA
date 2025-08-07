select distinct e.employee_id  from 
Employees  e
left join (
SELECT employee_id, MONTH(in_time) m, SUM(CEIL(TIMESTAMPDIFF(SECOND, in_time, out_time) / 60.0)) / 60  hours
FROM logs
group by employee_id,m
)
l on l.employee_id=e.employee_id
where ifnull(l.hours,0)<e.needed_hours 
order by 1