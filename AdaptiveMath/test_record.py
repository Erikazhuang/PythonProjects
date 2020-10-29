import pytest
import record
import database.dbaccess as db
from settings import DBCONNECTIONSTRING

def test_save_record():
    result = record.save_record_to_database(2,20200925105102,30,'2020-09-25',0)
    assert result

def test_get_record():
    result = record.get_records_by_userid(1)
    print(result)
    assert len(result)>0

def test_get_wrong_questions():
    records = record.get_records_by_userid(1)
    result = records[['questionid','result']].groupby('questionid', as_index=False,sort=False)['result'].sum()
    result= result.where('question')
    print(result)
    assert 1==1