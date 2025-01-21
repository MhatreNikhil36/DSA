# Write your MySQL query statement below
with cte as (select  num,lead(num) over (order by id) leadnum,lag(num) over (order by id) lagnum  from logs)
select distinct num ConsecutiveNums from cte where leadnum=lagnum and num=lagnum
