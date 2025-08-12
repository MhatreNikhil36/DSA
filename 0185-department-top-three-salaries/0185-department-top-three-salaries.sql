# Write your MySQL query statement below
with rnk_emp_salary as (
    select 
        name ,departmentid,salary , 
        dense_rank() over(partition by departmentid order by salary  desc) rnk
    from employee)

select d.name Department ,e.name Employee , e.salary
from 
    (select name,departmentid,salary ,rnk 
    from rnk_emp_salary ) e
 join Department d on e.departmentid=d.id
where e.rnk<4