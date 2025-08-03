select u.name, ifnull(t.balance,0) balance from 
users u inner join (
select account,sum(amount) balance
from transactions
group by account
having balance>10000
 ) t on u.account=t.account
