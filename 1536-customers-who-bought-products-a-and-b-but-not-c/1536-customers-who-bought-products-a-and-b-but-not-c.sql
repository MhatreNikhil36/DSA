# Write your MySQL query statement below
with a as (
    select distinct customer_id from Orders  where product_name='A'  
)
,b as(
    select distinct customer_id from Orders  where product_name='B'  
),
c as (
    select distinct customer_id from Orders  where product_name='C'  
)
select * from Customers where 
customer_id in (select customer_id from a) and customer_id in (select customer_id from b) and customer_id not in (select customer_id from c)  