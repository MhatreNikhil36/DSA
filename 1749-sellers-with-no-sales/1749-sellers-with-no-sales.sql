select s.seller_name  from
seller s
left join (
select  seller_id
from orders where EXTRACT(YEAR FROM sale_date) = 2020
) o
on  s.seller_id=o.seller_id
where o.seller_id is null
order by s.seller_name
