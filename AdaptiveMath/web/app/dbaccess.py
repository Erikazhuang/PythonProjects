import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

def create_connection(connectionstring):
    engine = create_engine(connectionstring)
    return engine

def read_dataframe_query(query, conn):
    df = pd.read_sql_query(query,conn)
    return df

def execute_query(query, conn):
    pass

