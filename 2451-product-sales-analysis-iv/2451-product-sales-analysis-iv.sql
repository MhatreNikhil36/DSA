# Write your MySQL query statement below
select user_id,product_id from (
select s.user_id,s.product_id
,rank() over( partition by s.user_id order by sum(p.price * s.quantity) desc) r
from  sales s
left join 
product p on p.product_id =s.product_id  
group by s.user_id,s.product_id
) a where r=1