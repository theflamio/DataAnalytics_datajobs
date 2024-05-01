# python/__init__.py

# Import modules to make them available when the package is imported
from .etl_main import main_etl_process
from .extractor import extract_data
from .transformer import transform_data
from .loader import load_data
from .config import DATABASE_URL

# Define package initialization
print("Initializing ETL package...")