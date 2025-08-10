WITH master_table AS (
    SELECT 
        t.transaction_id,
        t.customer_id,
        t.product_id,
        ROUND(t.amount, 2) AS amount,
        p.category,
        t.transaction_date
    FROM Transactions t
    JOIN Products p 
      ON t.product_id = p.product_id
),
agg_cus_stats AS (
    SELECT 
        customer_id,
        ROUND(SUM(amount), 2) AS total_amount,
        COUNT(transaction_id) AS transaction_count,
        COUNT(DISTINCT category) AS unique_categories,
        ROUND(AVG(amount), 2) AS avg_transaction_amount
    FROM master_table
    GROUP BY customer_id
),
cus_category_rnk AS (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY category_count DESC, last_purchase DESC
        ) AS rn
    FROM (
        SELECT 
            customer_id,
            category,
            COUNT(*) AS category_count,
            MAX(transaction_date) AS last_purchase
        FROM master_table
        GROUP BY customer_id, category
    ) sub
)
SELECT  
    a.customer_id,
    a.total_amount,
    a.transaction_count,
    a.unique_categories,
    a.avg_transaction_amount,
    c.category AS top_category,
    ROUND((a.transaction_count * 10) + (a.total_amount / 100), 2) AS loyalty_score
FROM agg_cus_stats a
LEFT JOIN cus_category_rnk c
    ON a.customer_id = c.customer_id AND c.rn = 1
ORDER BY loyalty_score DESC, a.customer_id ASC;
