with  pivot  as (
SELECT 
    i.item_category CATEGORY,
    case when WEEKDAY(order_date)=0 then SUM(quantity)  else 0 end  as MONDAY ,
    case when WEEKDAY(order_date)=1 then SUM(quantity)  else 0 end  as TUESDAY, 
    case when WEEKDAY(order_date)=2 then SUM(quantity)  else 0 end  as WEDNESDAY, 
    case when WEEKDAY(order_date)=3 then SUM(quantity)  else 0 end  as THURSDAY  ,
    case when WEEKDAY(order_date)=4 then SUM(quantity)  else 0 end  as FRIDAY  ,
    case when WEEKDAY(order_date)=5 then SUM(quantity)  else 0 end  as SATURDAY ,  
    case when WEEKDAY(order_date)=6 then SUM(quantity)  else 0 end  as SUNDAY  
from Items i
LEFT JOIN  Orders  os
    ON os.item_id = i.item_id
group by category,WEEKDAY(os.order_date)) 
select 
    CATEGORY, 
    sum(MONDAY) MONDAY,
    sum(TUESDAY ) TUESDAY ,
    sum(WEDNESDAY) WEDNESDAY,
    sum(THURSDAY ) THURSDAY ,
    sum(FRIDAY ) FRIDAY ,
    sum(SATURDAY ) SATURDAY ,
    sum(SUNDAY ) SUNDAY 
from pivot
group by category
order by category