import database.dbaccess as db
import pandas as pd
from datetime import datetime
from settings import DBCONNECTIONSTRING
import random

def generate_plus_questions_all(maxnum=20):
    questions = list()

    for x in range(0,maxnum + 1):
        if x>10:
            for y in range(0,11):
                questions.append( ("{0} + {1} = ".format(x,y), '{0}'.format(x + y),0,'basic calculation',datetime.now(),1) )
        else:
            for y in range(0,maxnum):
                questions.append( ("{0} + {1} = ".format(x,y),'{0}'.format(x + y),0,'basic calculation',datetime.now(),1) )

    df = pd.DataFrame(questions)
    df.columns = ['question','answer','level','type','datecreated','active']
    return df

def append_question_to_database(questiondf):
    conn = db.create_connection(DBCONNECTIONSTRING)
    questiondf.to_sql('questions',conn,if_exists='append',index_label='qid')

def replace_question_to_database(questiondf):
    conn = db.create_connection(DBCONNECTIONSTRING)
    questiondf.to_sql('questions',conn, if_exists='replace',index_label='qid')

def __get_all_questions():
    query = 'SELECT * FROM questions'
    conn = db.create_connection(DBCONNECTIONSTRING)
    result = db.read_dataframe_query(query,conn)
    return result

def get_random_questions(num):
    allquestions = __get_all_questions()
    #print(allquestions)
    randomquestions = list()

    for idx in random.sample(range(0,len(allquestions)),num):
        randomquestions.append(allquestions.iloc[idx][['qid','question','answer']])

    return randomquestions