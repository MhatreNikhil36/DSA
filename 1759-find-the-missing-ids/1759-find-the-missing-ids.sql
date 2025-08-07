WITH 
RECURSIVE seq AS (
    SELECT 1 aS value
    UNION ALL
    SELECT value + 1 FROM seq WHERE value + 1 <= (SELECT MAX(customer_id) AS max_val FROM Customers)
)
SELECT s.value AS ids
FROM seq s
LEFT JOIN Customers c ON c.customer_id = s.value
WHERE c.customer_id IS NULL;
