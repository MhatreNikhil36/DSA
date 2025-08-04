SELECT DISTINCT e1.employee_id
FROM Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id
LEFT JOIN Employees e3 ON e2.manager_id = e3.employee_id
LEFT JOIN Employees e4 ON e3.manager_id = e4.employee_id
WHERE 
    (e1.manager_id = 1 and e1.employee_id!=1) OR
    (e2.manager_id = 1 and e2.employee_id!=1)OR
    (e3.manager_id = 1 and e3.employee_id!=1)
