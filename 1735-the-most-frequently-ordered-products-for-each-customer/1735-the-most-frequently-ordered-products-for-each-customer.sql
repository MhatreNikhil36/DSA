WITH c AS (
  SELECT 
  distinct
    customer_id,
    product_id, COUNT(order_id) OVER (PARTITION BY customer_id, product_id) AS orderC
  FROM orders
)
SELECT 
  c.customer_id,
  c.product_id,
  p.product_name
FROM 
  c
JOIN 
  products p ON c.product_id = p.product_id
WHERE 
  (c.customer_id, c.orderC) IN (
    SELECT 
      customer_id,
      MAX(orderC)
    FROM 
      c
    GROUP BY 
      customer_id
  );
