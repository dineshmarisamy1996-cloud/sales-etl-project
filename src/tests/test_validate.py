import pytest

from etl.validate import validate_data


def test_validate_data_success(spark):

    data = [
        (1, "John", "Laptop", 2, 500.0),
        (2, "David", "Mouse", 3, 20.0),
        (3, "Kumar", "Keyboard", 1, 50.0)
    ]

    columns = [
        "OrderID",
        "Customer",
        "Product",
        "Qty",
        "Price"
    ]

    df = spark.createDataFrame(data, columns)

    result = validate_data(df)

    assert result.count() == 3


def test_validate_duplicate_order_id(spark):

    data = [
        (1, "John", "Laptop", 2, 500.0),
        (1, "David", "Mouse", 3, 20.0),
        (2, "Kumar", "Keyboard", 1, 50.0)
    ]

    columns = [
        "OrderID",
        "Customer",
        "Product",
        "Qty",
        "Price"
    ]

    df = spark.createDataFrame(data, columns)

    with pytest.raises(ValueError, match="Duplicate OrderIDs found"):
        validate_data(df)


def test_validate_negative_qty(spark):

    data = [
        (1, "John", "Laptop", -2, 500.0),
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

    with pytest.raises(ValueError, match="Negative Qty found"):
        validate_data(df)


def test_validate_negative_price(spark):

    data = [
        (1, "John", "Laptop", 2, -500.0),
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

    with pytest.raises(ValueError, match="Negative Price found"):
        validate_data(df)