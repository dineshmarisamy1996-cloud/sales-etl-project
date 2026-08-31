##  python -m pytest src/tests -v  --This query is for test the whole etl
##  python -m pytest src/tests/test_validate.py -v -- This is for test the specific part

"""

python -m pytest src/tests --cov=src/etl --cov-report=term-missing

You'll get something similar to:

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src/etl/extract.py      10      1    90%   25
src/etl/transform.py    15      0   100%
src/etl/validate.py     20      0   100%
src/etl/load.py          7      0   100%
--------------------------------------------------
TOTAL                   52      1    98%

"""

from etl.extract import extract_data
from config.config import INPUT_FILE
from schema.sales_schema import sales_schema
from pyspark.sql.types import (
        IntegerType,
        StringType,
        DoubleType
    )

def test_extract_data(spark):
        df = extract_data(
            spark,
            INPUT_FILE,
            sales_schema
        )
        ##assert means "check/verify that something is true.
        assert df is not None ##Test 1 → DataFrame created

def test_extract_columns(spark):
        df = extract_data(
            spark,
            INPUT_FILE,
            sales_schema
        )

        expected_columns = [
            "OrderID",
            "Customer",
            "Product",
            "Qty",
            "Price"
        ]

        assert df.columns == expected_columns ##Test 2 → Expected columns exist

def test_extract_schema(spark):
        df = extract_data(
            spark,
            INPUT_FILE,
            sales_schema
        )
       ##test whether Spark loaded your CSV with the correct data types.

        assert isinstance(df.schema["OrderID"].dataType, IntegerType)
        assert isinstance(df.schema["Customer"].dataType, StringType)
        assert isinstance(df.schema["Product"].dataType, StringType)
        assert isinstance(df.schema["Qty"].dataType, IntegerType)
        assert isinstance(df.schema["Price"].dataType, DoubleType)
def test_extract_row_count(spark):

    df = extract_data(
        spark,
        INPUT_FILE,
        sales_schema
    )

    assert df.count() == 13