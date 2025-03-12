# Write your MySQL query statement below
select customer_id from(
select customer_id,year ,sum(revenue) revenue   from Customers
group by customer_id,year
having year=2021 and revenue >0) a