SELECT SALE_DATE , SUM(
CASE 
WHEN FRUIT= 'apples' then 1*sold_num
when fruit='oranges' then -1*sold_num
else 0 END ) as diff
from sales
group by sale_date
