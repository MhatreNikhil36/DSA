select c.customer_id,c.name from  customers c
inner join(
select a.customer_id
from (
select o.customer_id,o.product_id,o.quantity*p.price as spent1   from  orders  o
left join  Product p
on p.product_id=o.product_id
WHERE EXTRACT(YEAR FROM order_date) = 2020
  AND EXTRACT(MONTH FROM order_date) IN (6)) a
inner  join 
 (
select o.customer_id,o.product_id,o.quantity*p.price as spent2     from  orders  o
left join  Product p
on p.product_id=o.product_id
WHERE EXTRACT(YEAR FROM order_date) = 2020
  AND EXTRACT(MONTH FROM order_date) IN (7)
  
  ) b on
  a.customer_id=b.customer_id
group by  a.customer_id
having sum(spent1)>=100 and sum(spent2)>=100
) b
on c.customer_id=b.customer_id

