select t.transaction_id from
(
select day,max(amount) mamount
from transactions
group by  day ) d
join 
transactions t on t.day=d.day
where t.amount=d.mamount
order by transaction_id 
