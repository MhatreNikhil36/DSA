# Write your MySQL query statement below
with maxsal as 
(
select  departmentId,name  as  employee ,salary, rank() over(  partition by departmentid order by  salary desc) as r
from employee

)

select name as department  ,employee, salary
from department inner join maxsal
on id=departmentId
and r=1
