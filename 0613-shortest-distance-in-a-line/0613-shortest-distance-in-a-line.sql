# Write your MySQL query statement below
select min(abs(greatest(a.x ,b.x)-least(a.x ,b.x)))  shortest 
from point a,point b
where a.x!=b.x