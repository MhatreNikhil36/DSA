WITH ranked AS (
    SELECT
        customer_id,
        transaction_date,
        amount,
        CASE 
            WHEN DATEDIFF(transaction_date, LAG(transaction_date) OVER (PARTITION BY customer_id ORDER BY transaction_date)) = 1
             AND amount > LAG(amount) OVER (PARTITION BY customer_id ORDER BY transaction_date)
            THEN 0
            ELSE 1
        END AS is_break
    FROM Transactions
),
grp_assign AS (
    SELECT
        customer_id,
        transaction_date,
        amount,
        SUM(is_break) OVER (PARTITION BY customer_id ORDER BY transaction_date ROWS UNBOUNDED PRECEDING) AS grp
    FROM ranked
)
SELECT
    customer_id,
    MIN(transaction_date) AS consecutive_start,
    MAX(transaction_date) AS consecutive_end
FROM grp_assign
GROUP BY customer_id, grp
HAVING COUNT(*) >= 3
ORDER BY customer_id, consecutive_start;
