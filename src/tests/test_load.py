import os
import tempfile

from etl.load import load_parquet


def test_load_parquet(spark):

    data = [
        (1, "John", "Laptop", 2, 500.0),
        (2, "David", "Mouse", 3, 20.0)
    ]

    columns = [
        "OrderID",
        "Customer",
        "Product",
        "Qty",
        "Price"
    ]

    df = spark.createDataFrame(data, columns)
   ##TemporaryDirectory()-- creates a temporary folder on your computer.
    ##We use a temporary folder in unit testing because we don't want the
    # test to write files into your real project output folder
    with tempfile.TemporaryDirectory() as temp_dir:
    ##C:\Users\dines\AppData\Local\Temp\tmpabc123\sales_parquet--below line output
        output_path = os.path.join(
            temp_dir,
            "sales_parquet"
        )

        load_parquet(df, output_path)

        # Verify output path exists
        assert os.path.exists(output_path)

        # Read the written Parquet file
        loaded_df = spark.read.parquet(output_path)

        # Verify record count
        assert loaded_df.count() == 2