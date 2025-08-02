# Write your MySQL query statement below
select student_id, course_id , grade from (
select student_id, course_id , grade, row_number() over( partition by student_id order by grade desc,course_id   ) as r
from Enrollments) a
where r=1

-- select student_id,course_id, grade from
-- enrollements  
-- group by student_id
-- order by 