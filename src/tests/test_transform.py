from etl.transform import clean_data, calculate_total


def test_clean_data_removes_null_customer_product(spark):

    data = [
        (1, "John", "Laptop", 2, 500.0),
        (2, None, "Mouse", 3, 20.0),
        (3, "David", None, 1, 100.0),
        (4, "Kumar", "Keyboard", 2, 50.0)
    ]

    columns = [
        "OrderID",
        "Customer",
        "Product",
        "Qty",
        "Price"
    ]

    df = spark.createDataFrame(data, columns)

    result = clean_data(df)

    assert result.count() == 2


def test_clean_data_fills_null_qty_price(spark):

    data = [
        (1, "John", "Laptop", None, None),
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

    result = clean_data(df)

    first_row = result.filter(
        result.OrderID == 1
    ).first()

    assert first_row.Qty == 0
    assert first_row.Price == 0


def test_clean_data_removes_duplicates(spark):

    data = [
        (1, "John", "Laptop", 2, 500.0),
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

    result = clean_data(df)

    assert result.count() == 2


def test_calculate_total(spark):

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

    result = calculate_total(df)

    first_row = result.filter(
        result.OrderID == 1
    ).first()

    second_row = result.filter(
        result.OrderID == 2
    ).first()

    assert first_row.TotalAmount == 1000.0
    assert second_row.TotalAmount == 60.0