# src/database/db_utils.py
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

def get_engine(db_url):
    return create_engine(db_url)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

def get_table_names(engine):
    inspector = inspect(engine)
    return inspector.get_table_names()

def get_column_types(engine, table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    return {col['name']: col['type'] for col in columns}

def get_table_data(session, table_name):
    query = f"SELECT * FROM {table_name}"
    result = session.execute(query)
    data = result.fetchall()
    columns = result.keys()
    return data, columns
