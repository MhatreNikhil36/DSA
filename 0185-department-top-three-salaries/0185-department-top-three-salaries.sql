with main as (select name         , departmentid, dense_rank() over(partition by  departmentid order by salary desc) r,salary  from employee 
order by salary desc)
select d.name  Department,main.name Employee ,Salary from main inner join department d
on d.id=main.departmentid
where main.r<=3