from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession.builder
    .appName("GoldLayer")
    .getOrCreate()
)

print("Spark Session Started")
silver_df = spark.read.csv(
    "data/silver/orders.csv",
    header=True,
    inferSchema=True
)

print("Silver Loaded")

silver_df.show(5)
daily_revenue = (
    silver_df
    .withColumn(
        "order_date",
        to_date(col("order_purchase_timestamp"))
    )
    .groupBy("order_date")
    .agg(
        sum("revenue").alias("daily_revenue")
    )
)

daily_revenue.show(5)
daily_revenue.toPandas().to_csv(
    "data/gold/daily_revenue.csv",
    index=False
)

print("Daily Revenue Saved")
# ==========================
# TOP PRODUCT CATEGORIES
# ==========================

top_categories = (
    silver_df
    .groupBy("product_category_name_english")
    .agg(
        sum("revenue").alias("total_revenue")
    )
    .orderBy(col("total_revenue").desc())
)

top_categories.show(10)

top_categories.toPandas().to_csv(
    "data/gold/top_product_categories.csv",
    index=False
)

print("Top Categories Saved")
# ==========================
# CUSTOMER RETENTION
# ==========================

customer_retention = (
    silver_df
    .groupBy("customer_unique_id")
    .count()
    .filter(col("count") > 1)
)

customer_retention.show(10)

customer_retention.toPandas().to_csv(
    "data/gold/customer_retention.csv",
    index=False
)

print("Customer Retention Saved")
from pyspark.sql.functions import datediff, avg, col

avg_delivery = (
    silver_df
    .withColumn(
        "delivery_days",
        datediff(
            col("order_delivered_customer_date"),
            col("order_purchase_timestamp")
        )
    )
    .groupBy("customer_state")
    .agg(
        avg("delivery_days").alias("avg_delivery_days")
    )
)

avg_delivery.show(10)

avg_delivery.toPandas().to_csv(
    "data/gold/avg_delivery_by_state.csv",
    index=False
)

print("Average Delivery Saved")