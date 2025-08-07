# Write your MySQL query statement below
select o.user_id,sum(p.price*o.quantity) as spending
from sales o
left join  product p on o.product_id=p.product_id
group by o.user_id
order by  2 desc, 1 asc
