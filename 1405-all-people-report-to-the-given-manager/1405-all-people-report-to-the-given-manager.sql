# Write your MySQL query statement below

with direct as (
select employee_id from employees where manager_id=1 and employee_id!=1)
, lvl2 as (
select employee_id from employees where manager_id in (select employee_id from direct))

select employee_id from employees where manager_id in (select employee_id from lvl2)
union all
select employee_id from direct
union all
select employee_id from lvl2
