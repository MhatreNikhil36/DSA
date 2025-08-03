-- select round(avg(order_date=customer_pref_delivery_date)*100 ,2) immediate_percentage 
-- from Delivery

select round(100*count(case when order_date=customer_pref_delivery_date then 1 end)/count(1) ,2) immediate_percentage 
from Delivery
