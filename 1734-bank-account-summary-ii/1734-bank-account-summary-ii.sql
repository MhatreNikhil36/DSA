select u.name, ifnull(t.balance,0) balance from 
users u left join (
select account,sum(amount) balance
from transactions
group by account
 ) t on u.account=t.account
 where t.balance>10000