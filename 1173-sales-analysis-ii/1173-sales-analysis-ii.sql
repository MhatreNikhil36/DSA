SELECT buyer_id
FROM Sales
JOIN product
USING(product_id)
GROUP BY buyer_id
HAVING SUM(CASE WHEN product_name = 'S8' THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN product_name = 'iPhone' THEN 1 ELSE 0 END) = 0;