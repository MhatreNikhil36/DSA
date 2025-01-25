# Write your MySQL query statement below
with od as (
    select product_id,sum(unit ) unit from orders 
    where year(order_date)='2020' and month(order_date)='02'
    group by product_id
        )
select product_name , od.unit from Products  inner join od 
on od.product_id=Products.product_id
where unit>=100