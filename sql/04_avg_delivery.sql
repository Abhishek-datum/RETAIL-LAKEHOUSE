SELECT
    AVG(DATEDIFF(order_delivered_customer_date,
                 order_purchase_timestamp)) AS avg_delivery_days
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;