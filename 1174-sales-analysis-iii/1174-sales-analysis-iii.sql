# Write your MySQL query statement below


select product_id,product_name  from Product p

where product_id in 
(select product_id from sales 
where sale_date    between '2019-01-01' and '2019-03-31')
and  product_id  not in
 (select product_id from sales 
where sale_date    not between '2019-01-01' and '2019-03-31') 

  