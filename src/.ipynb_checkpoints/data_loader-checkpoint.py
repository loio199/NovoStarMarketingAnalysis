import pandas as pd

from src.config import (
    CUSTOMERS_FILE,
    PRODUCTS_FILE,
    ORDERS_FILE,
    ORDER_ITEMS_FILE,
    CAMPAIGNS_FILE,
    SUPPORT_TICKETS_FILE,
)


def load_data():
    """
    Load all raw datasets and perform basic date parsing.

    Returns
    -------
    dict
        Dictionary containing all project datasets.
    """

    customers = pd.read_csv(
        CUSTOMERS_FILE
    )
    customers["signup_date"] = pd.to_datetime(
        customers["signup_date"],
        format="mixed")

    products = pd.read_csv(
        PRODUCTS_FILE,
        parse_dates=["launch_date"],
    )

    orders = pd.read_csv(
        ORDERS_FILE,
        parse_dates=["order_date"],
    )

    order_items = pd.read_csv(
        ORDER_ITEMS_FILE,
    )

    campaigns = pd.read_csv(
        CAMPAIGNS_FILE,
        parse_dates=["start_date", "end_date"],
    )

    support = pd.read_csv(
        SUPPORT_TICKETS_FILE,
        parse_dates=["created_at"],
    )

    return {
        "customers": customers,
        "products": products,
        "orders": orders,
        "order_items": order_items,
        "campaigns": campaigns,
        "support": support,
    }