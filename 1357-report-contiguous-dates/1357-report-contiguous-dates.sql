select period_state ,min(date) start_date ,max(date) end_date    from(
select *, row_number() over(order by date)- row_number() over(partition by  period_state order by date) grp
 from (
select success_date   date,'succeeded' as period_state from Succeeded
 where success_date between '2019-01-01'  and '2019-12-31'
union 
select fail_date date, 'failed' as period_state from failed
where fail_date between '2019-01-01'  and '2019-12-31'
) a
order by date ) a
group by grp,period_state