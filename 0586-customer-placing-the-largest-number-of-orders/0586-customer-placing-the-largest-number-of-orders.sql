select customer_number from (
select customer_number ,count(1) c
from orders 
group by customer_number 
order by c desc
limit 1) res