# Write your MySQL query statement below
with disProduct as (
    select count(product_key) as c from Product
)
select customer_id  from customer 
group by customer_id  
having count(distinct product_key)>=(select c from disProduct)