WITH RECURSIVE subordinates AS (
    -- Anchor: employees who report directly to the head
    SELECT employee_id
    FROM employees
    WHERE manager_id = 1 AND employee_id != 1

    UNION ALL

    -- Recursive: employees who report to those found so far
    SELECT e.employee_id
    FROM employees e
    JOIN subordinates s ON e.manager_id = s.employee_id
)
SELECT employee_id
FROM subordinates;
