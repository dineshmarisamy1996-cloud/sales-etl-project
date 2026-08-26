from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType
)

# ==========================================================
# SCHEMA
# ==========================================================

sales_schema = StructType([
    StructField("OrderID", IntegerType(), False),
    StructField("Customer", StringType(), True),
    StructField("Product", StringType(), True),
    StructField("Qty", IntegerType(), True),
    StructField("Price", DoubleType(), True)
])