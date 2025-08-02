
select s.name from SalesPerson s
left join (
select o.sales_id from orders o 
inner join Company c
on c.com_id  =o.com_id
where c.name='RED'

) redSales
on s.sales_id=redSales.sales_id
where redSales.sales_id is Null