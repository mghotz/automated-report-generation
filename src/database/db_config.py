# src/database/db_config.py
from config import DATABASE_URL
from .db_utils import get_engine, get_session, get_table_names, get_column_types

def init_db():
    engine = get_engine(DATABASE_URL)
    session = get_session(engine)
    return engine, session

def get_db_info():
    engine, session = init_db()
    table_names = get_table_names(engine)
    table_info = {table: get_column_types(engine, table) for table in table_names}
    return table_info
