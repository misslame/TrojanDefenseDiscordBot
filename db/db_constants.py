from pathlib import Path

# Get the root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Location of the SQLite database
DATABASE_PATH = BASE_DIR / "data"

# Location of the database schema
SCHEMA_PATH = BASE_DIR / "db" / "schema.sql"