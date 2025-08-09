SELECT 
    i.item_category AS category,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 0 THEN os.quantity ELSE 0 END) AS monday,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 1 THEN os.quantity ELSE 0 END) AS tuesday,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 2 THEN os.quantity ELSE 0 END) AS wednesday,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 3 THEN os.quantity ELSE 0 END) AS thursday,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 4 THEN os.quantity ELSE 0 END) AS friday,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 5 THEN os.quantity ELSE 0 END) AS saturday,
    SUM(CASE WHEN WEEKDAY(os.order_date) = 6 THEN os.quantity ELSE 0 END) AS sunday
FROM Items i
LEFT JOIN Orders os
    ON os.item_id = i.item_id
GROUP BY i.item_category
ORDER BY i.item_category;
