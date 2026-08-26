import logging
from config.config import INPUT_FILE
from schema.sales_schema import sales_schema


logger = logging.getLogger(__name__)
def extract_data(spark, input_file, schema):
    logger.info("Reading input CSV file...")

    df = spark.read.csv(
    input_file,
    header=True,
    schema=schema
    )

    logger.info(f"Original Records: {df.count()}")
    df.show()
    return df