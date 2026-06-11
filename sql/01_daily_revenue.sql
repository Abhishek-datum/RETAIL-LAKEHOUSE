SELECT
DATE(order_purchase_timestamp) AS order_date,
SUM(revenue) AS daily_revenue
FROM silver_orders
GROUP BY DATE(order_purchase_timestamp)
ORDER BY order_date;