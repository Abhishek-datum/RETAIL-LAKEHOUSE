SELECT
customer_state,
AVG(
DATEDIFF(
order_delivered_customer_date,
order_purchase_timestamp
)
) AS avg_delivery_days
FROM silver_orders
GROUP BY customer_state
ORDER BY avg_delivery_days;