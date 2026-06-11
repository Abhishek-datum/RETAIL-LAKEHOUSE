SELECT
payment_type,
COUNT(*) AS total_orders,
SUM(payment_value) AS total_payment
FROM silver_orders
GROUP BY payment_type
ORDER BY total_orders DESC;