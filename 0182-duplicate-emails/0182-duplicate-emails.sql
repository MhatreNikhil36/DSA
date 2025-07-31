# Write your MySQL query statement below
select email from(
select email, row_number() over(partition by email) as  rn
from person 
where email is not null
) as emails
where rn=2
