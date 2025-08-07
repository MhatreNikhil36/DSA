# Write your MySQL query statement below
with agg_sales as (
select seller_id,sum(price) t_sales
from sales
group by seller_id )
select seller_id from agg_sales 
where t_sales=(select max(t_sales) from agg_sales)
