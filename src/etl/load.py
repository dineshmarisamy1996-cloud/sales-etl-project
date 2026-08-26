import logging


logger = logging.getLogger(__name__)
logger.info("Writing parquet file...")
def load_parquet(df, output_path):
        df.write.mode("overwrite").parquet(output_path)
        logger.info("Parquet file written successfully")
        logger.info("===== ETL Job Completed Successfully =====")