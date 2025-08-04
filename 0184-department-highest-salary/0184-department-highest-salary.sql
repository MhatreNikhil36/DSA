select d.name department, e.employee, e.salary
from department d join 
(
select departmentId, name employee ,salary,rank() over( partition by departmentId order by salary desc ) rn
from employee
) e
on d.id=e.departmentId
where e.rn=1