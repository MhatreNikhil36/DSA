# Write your MySQL query statement below
select min(abs(a.x -b.x))  shortest 
from point a,point b
where a.x!=b.x