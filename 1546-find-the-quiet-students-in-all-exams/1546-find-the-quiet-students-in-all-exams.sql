
select s.student_id,s.student_name from student s
join 
(

select q.student_id , sum(case when q.score  between e.low+1 and e.high-1 then 0 else 1  end) as notquite
from exam q
left join 
(select exam_id, min(score) low, max(score) high 
from exam group by exam_id) e 
on q.exam_id =e.exam_id
group by q.student_id
) e
on s.student_id=e.student_id 
where notquite=0