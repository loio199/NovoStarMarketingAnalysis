from pathlib import Path


# ---------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------

# config.py is located at:
# NovoStarMarketingAnalysis/src/config.py
#
# parents[1] therefore points to:
# NovoStarMarketingAnalysis/

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"


# ---------------------------------------------------------------------
# Raw data files
# ---------------------------------------------------------------------

CUSTOMERS_FILE = RAW_DATA_DIR / "customers.csv"
PRODUCTS_FILE = RAW_DATA_DIR / "products.csv"
ORDERS_FILE = RAW_DATA_DIR / "orders.csv"
ORDER_ITEMS_FILE = RAW_DATA_DIR / "order_items.csv"
CAMPAIGNS_FILE = RAW_DATA_DIR / "campaigns.csv"
SUPPORT_TICKETS_FILE = RAW_DATA_DIR / "support_tickets.csv"

DATA_DICTIONARY_FILE = RAW_DATA_DIR / "DATA_DICTIONARY.md"


# ---------------------------------------------------------------------
# Create output directories if they don't exist
# ---------------------------------------------------------------------

OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)