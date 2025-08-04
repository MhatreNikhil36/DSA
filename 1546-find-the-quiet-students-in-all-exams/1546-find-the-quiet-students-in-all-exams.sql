SELECT s.student_id, s.student_name
FROM student s
JOIN (
    SELECT e.student_id
    FROM exam e
    JOIN (
        SELECT exam_id, MIN(score) AS low, MAX(score) AS high
        FROM exam
        GROUP BY exam_id
    ) r ON e.exam_id = r.exam_id
    GROUP BY e.student_id
    HAVING SUM(
        CASE 
            WHEN e.score = r.low OR e.score = r.high THEN 1 
            ELSE 0 
        END
    ) = 0
) quiet_students ON s.student_id = quiet_students.student_id
ORDER BY s.student_id;
