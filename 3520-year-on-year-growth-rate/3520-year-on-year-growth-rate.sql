# Write your MySQL query statement below
with year_spend_agg as (
    select product_id,
        extract(year  from transaction_date) as t_year,
        sum(spend) curr_year_spend
    from user_transactions
    group by product_id,t_year
)
select t_year  as year,product_id,
    curr_year_spend,
    lag(curr_year_spend) over(partition by  product_id order by t_year) prev_year_spend,
    round(((curr_year_spend-lag(curr_year_spend) over(partition by  product_id order by t_year))/
            lag(curr_year_spend) over(partition by  product_id order by t_year))*100,2) yoy_rate 
from year_spend_agg