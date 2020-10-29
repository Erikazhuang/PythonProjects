import pytest
import question
from datetime import datetime
import pandas as pd

def test_generate_plus_questions_all():
    generatedquestion = question.generate_plus_questions_all()
    print(generatedquestion)
    assert len(generatedquestion) == 330


def test_replace_plus_questions():
    df = question.generate_plus_questions_all()
    df['type'] = 'basic calculation plus'
    question.replace_question_to_database(df)
    assert len(df) == 330



def test_append_questions():
    df=pd.DataFrame({'question':'11-4=','answer':7,'level':0,'type':'basic calculation minus','datecreated':datetime.now(),'active':1})
    question.append_question_to_database(df)
    assert 1==1

def test_get_random_questions():
    qlist = question.get_random_questions(10)
    print(qlist)
    assert len(qlist) == 10