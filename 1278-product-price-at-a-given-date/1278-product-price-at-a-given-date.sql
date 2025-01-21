# Write your MySQL query statement below
with d as (
select product_id,new_price ,change_date , row_number() over(partition by product_id order by change_date desc,new_price desc)  rn  from  Products 
where change_date <'2019-08-17')
select product_id, 10 as price from products where 
product_id not in (select product_id from d)
union
select product_id,new_price as price from d where rn=1
order by product_id
