# Write your MySQL query statement below
select distinct user_id from (
select user_id,  ifnull(datediff(purchase_date,lag(purchase_date ) over(partition by user_id order by purchase_date)),10) diff
from purchases
) a 
where diff<=7
