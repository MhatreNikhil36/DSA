select product_id,sum(quantity) as total_quantity 
from sales
group by 1