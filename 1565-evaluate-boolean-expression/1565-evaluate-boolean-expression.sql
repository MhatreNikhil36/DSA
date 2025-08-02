# Write your MySQL query statement below
select e.left_operand , e.operator,e.right_operand, case 
when e.operator='=' and ifnull(va.value,0)=ifnull(vb.value,0) then 'true' 
when e.operator='<' and ifnull(va.value,0)<ifnull(vb.value,0) then 'true'  
when e.operator='>' and ifnull(va.value,0)>ifnull(vb.value,0) then 'true' 
Else 'false'
end as value from
Expressions e
left join Variables va  on va.name=e.left_operand  
left join Variables vb on  vb.name=e.right_operand  
