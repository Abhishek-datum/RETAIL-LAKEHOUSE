WITH customer_orders AS
(
    SELECT
        customer_unique_id,
        COUNT(DISTINCT order_id) AS order_count
    FROM orders
    GROUP BY customer_unique_id
)

SELECT
    COUNT(CASE WHEN order_count > 1 THEN 1 END) * 100.0 /
    COUNT(*) AS retention_percentage
FROM customer_orders;

