# Write your MySQL query statement below
select name Customers from customers where id not in (select customerId   from Orders)