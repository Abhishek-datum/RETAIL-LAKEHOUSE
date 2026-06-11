import os
import shutil

landing_path = "data/landing"
bronze_path = "data/bronze/orders"

# Read all files from landing
for file in os.listdir(landing_path):

    if file.endswith(".csv"):

        # Extract date from filename
        load_date = file.replace(
            "orders_",
            ""
        ).replace(
            ".csv",
            ""
        )

        # Create partition folder
        target_folder = (
            f"{bronze_path}/load_date={load_date}"
        )

        os.makedirs(
            target_folder,
            exist_ok=True
        )

        # Source file
        source_file = (
            f"{landing_path}/{file}"
        )

        # Destination file
        destination_file = (
            f"{target_folder}/{file}"
        )

        # Copy file
        shutil.copy(
            source_file,
            destination_file
        )

        print(
            f"Loaded {file}"
        )

print(
    "Bronze ingestion completed!"
)