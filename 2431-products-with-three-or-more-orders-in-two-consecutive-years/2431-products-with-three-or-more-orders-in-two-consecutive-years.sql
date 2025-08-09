# Write your MySQL query statement below
-- find the  order  per  pridt  for  each ear
-- for  a window of 2  consecutive  years  check if  sum is  >= 3

with a_orders_year as(
select product_id    , extract(year from purchase_date) o_year, count(order_id) o_count
from orders
group by product_id,o_year
order by  product_id,o_year
)

, a_orders_con_years as (
select  
    product_id,  o_year-lag(o_year) over(partition by product_id order by o_year) f_con,
    case when o_count>=3 and lag(o_count) over(partition by product_id order by o_year)>=3 then 1 else 0 end f_limit
    from a_orders_year

)
select distinct product_id  from a_orders_con_years where f_con=1 and f_limit=1


