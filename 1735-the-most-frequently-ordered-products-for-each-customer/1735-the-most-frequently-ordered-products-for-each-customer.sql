
select  c.customer_id,o.product_id,p.product_name
from
customers c
left join 
(
select customer_id,product_id, rank() over(partition  by customer_id order  by pc desc ) as r from
(
select  customer_id,product_id, count(product_id) pc
from orders
group by  customer_id,product_id
) a
) o on o.customer_id=c.customer_id
inner join products p on p.product_id=o.product_id
 where o.r=1
 and o.product_id  is not null