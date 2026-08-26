from config.config import (
    INPUT_FILE,
    OUTPUT_PATH,
    LOG_FILE,
    APP_NAME,
    HADOOP_HOME
)
from etl.extract import extract_data
from etl.transform import clean_data, calculate_total
from etl.validate import validate_data
from etl.load import load_parquet

from schema.sales_schema import sales_schema

import os
import logging

os.environ["HADOOP_HOME"] = HADOOP_HOME
os.environ["PATH"] += os.pathsep + os.path.join(HADOOP_HOME, "bin")

from pyspark.sql import SparkSession

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)




# ==========================================================
# MAIN ETL FUNCTION
# ==========================================================

def main():


 spark = None

# --------------------------------------------------
# CREATE SPARK SESSION
# --------------------------------------------------

 try:

    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master("local[*]")
        # .config("spark.hadoop.io.native.lib.available", "false")
        .getOrCreate()
    )

    logger.info("Spark Session Created")
    logger.info("===== Starting ETL Job =====")

    # ==========================================================
    # EXTRACT
    # ==========================================================

    df = extract_data(
        spark,
        INPUT_FILE,
        sales_schema
    )


    # ==========================================================
    # TRANSFORM
    # ==========================================================
    df = clean_data(df)

    validate_data(df)

    df = calculate_total(df)

    # ==========================================================
    # LOAD
    # ==========================================================
    load_parquet(df, OUTPUT_PATH)

    # ======================================================
    # EXCEPTION HANDLING
    # ======================================================

 except Exception as e:

    # Log complete error and traceback
    logger.exception("===== ETL Job Failed =====")
    logger.exception(f"Error: {e}")

    # Re-raise the exception so the job is marked as FAILED
    raise
    # ======================================================
    # CLEANUP
    # ======================================================

 finally:

    # This block executes whether ETL succeeds or fails
    if spark is not None:
        logger.info("Stopping Spark Session...")
        spark.stop()
        logger.info("Spark Session stopped")

    logger.info("===== ETL Job Ended =====")


# ==========================================================
# PROGRAM ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    main()