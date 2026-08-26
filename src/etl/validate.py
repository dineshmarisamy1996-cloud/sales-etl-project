import logging
logger = logging.getLogger(__name__)
def validate_data(df):

    duplicate_count = (
        df.groupBy("OrderID")
          .count()
          .filter("count > 1")
          .count()
    )

    if duplicate_count > 0:
        logger.error(f"Found {duplicate_count} duplicate OrderID(s)")
        raise ValueError("Duplicate OrderIDs found")

    negative_qty_count = df.filter(df.Qty < 0).count()

    if negative_qty_count > 0:
        logger.error(f"Found {negative_qty_count} negative Qty record(s)")
        raise ValueError("Negative Qty found")

    negative_price_count = df.filter(df.Price < 0).count()

    if negative_price_count > 0:
        logger.error(f"Found {negative_price_count} negative Price record(s)")
        raise ValueError("Negative Price found")

    logger.info("Data validation passed.")

    return df