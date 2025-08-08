# Write your MySQL query statement below
-- did  not  work  for  a previos  moth then that  months salary
--  did  work  for  consicutive  omnths then  cumulative  salary
--  do not include the latest  month 


select id,month ,sum(salary) over(partition by id,grp order by month 
 ROWS BETWEEN 2 PRECEDING AND CURRENT ROW ) as Salary  
from
(
select id,month,salary,month  - row_number() over(partition by id order by month) grp,
lead(month)over(partition by id order by month) f
from Employee
order by id,month) a
where f is not  null
order  by id, month desc