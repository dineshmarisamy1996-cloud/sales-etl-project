import os

#BASE_DIR it's just finding your project's root folder.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(BASE_DIR, "data", "sales.csv")

OUTPUT_PATH = os.path.join(BASE_DIR, "output", "sales_parquet")

LOG_FILE = os.path.join(BASE_DIR, "utils", "sales_etl.log")

APP_NAME = "SalesETL"

HADOOP_HOME = r"C:\hadoop"