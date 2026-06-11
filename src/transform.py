from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# ==========================
# SPARK SESSION
# ==========================

spark = (
    SparkSession.builder
    .appName("RetailLakehouse")
    .getOrCreate()
)

print("Spark Session Created Successfully")

# ==========================
# ORDERS DATASET
# ==========================

orders_df = spark.read.csv(
    "data/raw/olist_orders_dataset.csv",
    header=True,
    inferSchema=True
)

print("\nOrders Loaded")

orders_clean_df = orders_df.dropDuplicates()

print("\nOriginal Rows:")
print(orders_df.count())

print("\nRows After Deduplication:")
print(orders_clean_df.count())

# ==========================
# NULL CHECK
# ==========================

print("\nNull Count")

null_df = orders_clean_df.select([
    col(c).isNull().cast("int").alias(c)
    for c in orders_clean_df.columns
])

null_df.groupBy().sum().show()

# ==========================
# CUSTOMERS DATASET
# ==========================

customers_df = spark.read.csv(
    "data/raw/olist_customers_dataset.csv",
    header=True,
    inferSchema=True
)

silver_df = orders_clean_df.join(
    customers_df,
    on="customer_id",
    how="left"
)

print("\nOrders + Customers Join Completed")

# ==========================
# ORDER ITEMS DATASET
# ==========================

items_df = spark.read.csv(
    "data/raw/olist_order_items_dataset.csv",
    header=True,
    inferSchema=True
)

silver_df = silver_df.join(
    items_df,
    on="order_id",
    how="left"
)

print("\nOrder Items Join Completed")

# ==========================
# REVENUE COLUMN
# ==========================

silver_df = silver_df.withColumn(
    "revenue",
    col("price") + col("freight_value")
)

print("\nRevenue Column Created")

# ==========================
# PRODUCTS DATASET
# ==========================

products_df = spark.read.csv(
    "data/raw/olist_products_dataset.csv",
    header=True,
    inferSchema=True
)

silver_df = silver_df.join(
    products_df,
    on="product_id",
    how="left"
)

print("\nProducts Join Completed")

# ==========================
# PRODUCT TRANSLATION
# ==========================

translation_df = spark.read.csv(
    "data/raw/product_category_name_translation.csv",
    header=True,
    inferSchema=True
)

silver_df = silver_df.join(
    translation_df,
    on="product_category_name",
    how="left"
)

print("\nProduct Translation Join Completed")

# ==========================
# PAYMENTS DATASET
# ==========================

payments_df = spark.read.csv(
    "data/raw/olist_order_payments_dataset.csv",
    header=True,
    inferSchema=True
)

silver_df = silver_df.join(
    payments_df,
    on="order_id",
    how="left"
)

print("\nPayments Join Completed")

print("\nPayments Join Completed")

# ==========================
# REVIEWS DATASET
# ==========================

reviews_df = spark.read.csv(
    "data/raw/olist_order_reviews_dataset.csv",
    header=True,
    inferSchema=True
)

print("\nReviews Loaded")

silver_df = silver_df.join(
    reviews_df,
    on="order_id",
    how="left"
)

print("\nReviews Join Completed")

# ==========================
# SELLERS DATASET
# ==========================

sellers_df = spark.read.csv(
    "data/raw/olist_sellers_dataset.csv",
    header=True,
    inferSchema=True
)

print("\nSellers Loaded")

silver_df = silver_df.join(
    sellers_df,
    on="seller_id",
    how="left"
)

print("\nSellers Join Completed")
# ==========================
# OUTPUT
# ==========================

print("\nSilver Data Sample")

silver_df.show(5)

print("\nSilver Schema")

silver_df.printSchema()

# ==========================
# SAVE SILVER LAYER
# ==========================

print("\nSilver Data Sample")
silver_df.show(5)

print("\nSilver Schema")
silver_df.printSchema()

silver_df.toPandas().to_csv(
    "data/silver/orders.csv",
    index=False
)

print("\nSilver Layer Saved Successfully")

spark.stop()
