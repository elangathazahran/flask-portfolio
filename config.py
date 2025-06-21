import os

SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")

MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_DB = os.environ.get("MYSQL_DB", "portfolio_db")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False