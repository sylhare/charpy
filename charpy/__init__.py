import os

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(ROOT_PATH, "data")
MOCK_PATH = os.path.join(DATA_PATH, "mock")
SQL_PATH = os.path.join(DATA_PATH, "sql")

CHARPY_SQL = os.path.join(SQL_PATH, "charpy.db")

README_RST_PATH = os.path.join(ROOT_PATH, "README.rst")
README_MD_PATH = os.path.join(ROOT_PATH, os.path.join("docs", "README.md"))
