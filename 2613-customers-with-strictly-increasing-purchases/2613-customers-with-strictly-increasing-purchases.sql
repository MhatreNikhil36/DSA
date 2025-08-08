# Write your MySQL query statement below
--  sum per  year if  null then 0
--  first  year  will  be  the  first  year  of the  order 
--  last  year  of their  order 

with agg_purchase as(
select customer_id, extract(year  from order_date) as  f_year,sum(price) f_spent
from orders
group by customer_id,f_year
)

select customer_id from (
select  customer_id , f_year,
case  when f_spent>ifnull(lag(f_spent) over(partition by customer_id order by f_year asc) +1,-1) then 1
else 0 end as  inc_flag,
case  when f_year-ifnull(lag(f_year) over(partition by customer_id order by f_year asc),f_year- 1) <=1 then 1
else 0 end as  con_flag
from agg_purchase) m
group by  customer_id
having min(inc_flag)>=1  and min(con_flag)>=1
