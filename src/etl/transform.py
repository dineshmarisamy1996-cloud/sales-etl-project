import logging
from pyspark.sql.functions import col
# Data transformation logic
logger = logging.getLogger(__name__)
def clean_data(df):
    logger.info("Cleaning data")
    df = df.na.drop(subset=["Customer", "Product"])

    logger.info(
        f"Records after dropping null values: {df.count()}"
    )

    # Remove duplicate rows
    df = df.dropDuplicates()

    logger.info(
        f"Records after dropping duplicate values: {df.count()}"
    )

    # Replace NULL Qty with 0
    df = df.na.fill({
         "Qty": 0,
         "Price": 0
    })
    logger.info("Running data validation")
    return df

    # Add TotalAmount column
def calculate_total(df):
    logger.info("Calculating TotalAmount")
    df = df.withColumn(
        "TotalAmount",
        col("Qty") * col("Price")
    )

    logger.info("===== Processed Data =====")
    df.show()
    return df
