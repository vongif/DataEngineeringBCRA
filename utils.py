
from configparser import ConfigParser
from pathlib import Path
from sqlalchemy import create_engine


def lectura_de_credenciales_api(config_file: Path, section: str)-> dict:
    config = ConfigParser()
    config.read(config_file)
    credenciales_api = dict(config[section])
    return credenciales_api


def read_config_file(file_path: str) -> ConfigParser:
    config = ConfigParser()
    config.read(file_path)
    return config

def build_conn_string(config: ConfigParser, section: str, dbengine: str) -> str:
    host = config.get(section, "host")
    port = config.get(section, "port")
    user = config.get(section, "username")
    password = config.get(section, "pwd")
    database = config.get(section, "dbname")
    conn_str = f"{dbengine}://{user}:{password}@{host}:{port}/{database}"
    return conn_str

def connect_to_db(conn_str: str):
    engine = create_engine(conn_str)
    conn = engine.connect()
    return conn







