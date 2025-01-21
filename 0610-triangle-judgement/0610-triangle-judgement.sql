# Write your MySQL query statement below
select x,y,z,
case 
    when x<y+z and y<x+z  and z<y+x then 'Yes'
else 'No' END as  triangle
from Triangle 