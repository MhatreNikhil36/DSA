select p.product_name,p.product_id,o.order_id,o.order_date from
products p
left join 
(

select product_id, order_id,order_date,rank() over (partition by product_id order by  order_date desc) as rn
from Orders
)o 
on o.product_id=p.product_id 
where o.rn=1
order by p.product_name,p.product_id,o.order_id
