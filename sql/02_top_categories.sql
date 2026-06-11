SELECT
product_category_name_english,
SUM(revenue) AS total_revenue
FROM silver_orders
GROUP BY product_category_name_english
ORDER BY total_revenue DESC
LIMIT 10;