WITH sales_summary AS (
    SELECT 
        product_id,
        MIN(sale_date) as first_sale,
        MAX(sale_date) as last_sale
    FROM sales
    WHERE product_id IS NOT NULL
    GROUP BY product_id
)
SELECT p.product_id, p.product_name
FROM Product p
INNER JOIN sales_summary ss ON p.product_id = ss.product_id
WHERE ss.first_sale >= '2019-01-01' 
  AND ss.last_sale <= '2019-03-31'