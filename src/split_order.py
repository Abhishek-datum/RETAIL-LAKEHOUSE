import pandas as pd
import os

# Read orders dataset
orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

# Convert timestamp to datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Extract date
orders["order_date"] = (
    orders["order_purchase_timestamp"]
    .dt.date
)

# Create landing folder if not exists
os.makedirs(
    "data/landing",
    exist_ok=True
)

# Split by date
for day, group in orders.groupby("order_date"):

    file_name = (
        f"data/landing/orders_{day}.csv"
    )

    group.to_csv(
        file_name,
        index=False
    )

print("Daily files created successfully!")