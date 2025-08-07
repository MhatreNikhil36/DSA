# Write your MySQL query statement below
select seller_id  from (
select seller_id,sum(price) t_sales, rank() over( order by sum(price) desc ) r
from sales
group by seller_id) a
where r=1