with manages as (
    select reports_to as m_id, count(employee_id) as c, round(avg(age )) a_age from employees
    where reports_to is not NULL
    group by reports_to
)
select m_id employee_id , e.name, c as reports_count, a_age as average_age from manages inner join employees e
where m_id=e.employee_id
order by employee_id