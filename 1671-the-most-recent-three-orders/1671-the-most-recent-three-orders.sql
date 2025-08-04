select c.name as customer_name, c.customer_id, o.order_id,o.order_date
from customers c
left join 
(select customer_id,order_id,order_date, row_number() over(partition by customer_id order by order_date desc) rn
from orders
) as o
on  o.customer_id=c.customer_id
where o.rn<4 and o.customer_id is not null
order by c.name, c.customer_id,o.order_date desc