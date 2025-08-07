# Write your MySQL query statement below
select u.buyer_id from sales u
join (
select product_id , case when product_name='S8' then 1 else 0 end as is_s8
from product  where product_name='S8' or product_name='iPhone')p 
on p.product_id=u.product_id
group by u.buyer_id
having count(1)=sum(is_s8)

