# Write your MySQL query statement below


select u.user_id buyer_id ,u.join_date, count(order_id) orders_in_2019 
from users u
left join (
    select order_id,order_date ,buyer_id
    from orders 
    where extract(year from order_date)=2019) o

on  o.buyer_id=u.user_id
group by u.user_id