import pytest
import database.dbaccess as db

def setup_module(module):
    print('setup_module    module:%s' % module.__name__)

def test_getdataframe():
    engine = db.create_engine('sqlite:///database/adapt_math.db')
    df = db.read_dataframe_query("select * from records where id = 4", engine)
    test = df['result'][0]
    assert test == 0
