# Write your MySQL query statement below
with lim as (select case when count(id)%2=0 then count(id) else count(id)-1 end as lim from seat)
select  id, case 
when id%2=0 then lag(student) over(order by id) 
else lead(student) over(order by id ) end as student
from seat
where id <=(select lim id from lim)

union 
select id,student from seat where id>(select lim from lim)
order by id 