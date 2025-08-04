# Write your MySQL query statement below
select distinct title from  content c
 left join
(
select content_id,program_date  from   
tvprogram  
where extract(year from program_date)=2020  and extract(month from program_date)=6  
) t
on t.content_id=c.content_id
where c.Kids_content='Y'  and content_type ='Movies' 
and t.content_id is not null