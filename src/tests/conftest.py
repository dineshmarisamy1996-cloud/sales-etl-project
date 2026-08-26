import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    """
    Create a SparkSession for the test session.
    The same SparkSession will be reused by all tests.
    """

    spark = (
        SparkSession.builder
        .appName("SalesETL-UnitTests")
        .master("local[2]")
        .getOrCreate()
    )

    yield spark

    spark.stop()