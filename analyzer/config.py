import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from analyzer import gateway
from analyzer import analyzer_utils

analyzer_config = {}
analyzer_config["ENVIRONMENT"] = os.environ["ENVIRONMENT"] if "ENVIRONMENT" in os.environ.keys() else "local"
analyzer_config["DB_TYPE"] = os.environ["DB_TYPE"] if "DB_TYPE" in os.environ.keys() else "postgres"
analyzer_config["POSTGRES_HOST"] = os.environ["POSTGRES_HOST"] if "POSTGRES_HOST" in os.environ.keys() else "localhost"
analyzer_config["POSTGRES_PORT"] = os.environ["POSTGRES_PORT"] if "POSTGRES_PORT" in os.environ.keys() else "25432"
analyzer_config["POSTGRES_DB"] = os.environ["POSTGRES_DB"] if "POSTGRES_DB" in os.environ.keys() else "analyzer"
analyzer_config["POSTGRES_USER"] = os.environ["POSTGRES_USER"] if "POSTGRES_USER" in os.environ.keys() else "analyzer"
analyzer_config["POSTGRES_PASSWORD"] = (
    os.environ["POSTGRES_PASSWORD"] if "POSTGRES_PASSWORD" in os.environ.keys() else "analyzer"
)

env = analyzer_config["ENVIRONMENT"].upper()


def devMode():
    return env == "LOCAL" or env == "TEST"


analyzer_config["POSTGRES_HOST"] = (
    "localhost" if len(analyzer_config["POSTGRES_HOST"]) == 0 else analyzer_config["POSTGRES_HOST"]
)
analyzer_config["POSTGRES_PORT"] = (
    "25432" if len(analyzer_config["POSTGRES_PORT"]) == 0 else analyzer_config["POSTGRES_PORT"]
)
analyzer_config["POSTGRES_DB"] = (
    "analyzer" if len(analyzer_config["POSTGRES_DB"]) == 0 else analyzer_config["POSTGRES_DB"]
)
analyzer_config["POSTGRES_USER"] = (
    "analyzer" if len(analyzer_config["POSTGRES_USER"]) == 0 else analyzer_config["POSTGRES_USER"]
)
analyzer_config["POSTGRES_PASSWORD"] = (
    "analyzer" if len(analyzer_config["POSTGRES_PASSWORD"]) == 0 else analyzer_config["POSTGRES_PASSWORD"]
)

DATABASE_URL = f'postgresql+pg8000://{analyzer_config["POSTGRES_USER"]}:{analyzer_config["POSTGRES_PASSWORD"]}@{analyzer_config["POSTGRES_HOST"]}:{analyzer_config["POSTGRES_PORT"]}/analyzer'

try:
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

except Exception as error_instance:
    analyzer_utils.log_error(
        error_instance,
        "CREATING_ENGINE_DATABASE_EXCEPTION",
    )
