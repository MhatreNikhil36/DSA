# Write your MySQL query statement below
with a  as(
    select first_col, row_number() over(order by first_col   ) as  rn
    from Data 
), b
 as(
    select second_col , row_number() over(order by second_col   desc  ) as  rn
    from Data 
)

select a.first_col,b.second_col
from a
join b 
where a.rn=b.rn