SELECT transaction_id
FROM (
    SELECT 
        transaction_id,
        rank() OVER (PARTITION BY day ORDER BY amount DESC) AS rn
    FROM transactions
) r
WHERE rn = 1
ORDER BY transaction_id;
