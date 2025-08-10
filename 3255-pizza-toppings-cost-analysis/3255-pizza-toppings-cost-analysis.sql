# Write your MySQL query statement below


select  distinct
    concat(a.topping_name,',',b.topping_name,',',c.topping_name) pizza  , 
    round(a.cost +b.cost+c.cost,2) total_cost 
from Toppings a
join Toppings b on a.topping_name<b.topping_name
join Toppings c on b.topping_name<c.topping_name
where 
    a.topping_name<>b.topping_name and
    a.topping_name<>c.topping_name and 
    b.topping_name<>c.topping_name
order by total_cost desc,pizza